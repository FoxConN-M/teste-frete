from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional

from .models import QuoteRequest, QuoteResponse

TWOPLACES = Decimal("0.01")

@dataclass(frozen=True)

class BaseCarrier:
    name: str
    constant: Decimal
    min_height: int
    max_height: int
    min_width: int
    max_width: int
    delivery_days: int

    def is_eligible(self, req: QuoteRequest) -> bool:
        h = req.dimention.height
        w = req.dimention.widht
        return (
            self.min_height <= h <= self.max_height
            and self.min_width <= w <= self.max_width
            and req.weight > 0
        )
    
    def quote(self, req: QuoteRequest) -> Optional[QuoteResponse]:
        if not self.is_eligible(req):
            return None
        # (weight * constant / 10) -> duas casas decimais
        raw = (Decimal(req.weight) * self.constant) / Decimal(10)
        amount = raw.quantize(TWOPLACES, rounding=ROUND_HALF_UP)
        return QuoteResponse.model_construct(
            nome=self.name,
            valor_frete=amount,
            prazo_dias=self.delivery_days,
        )

# Catalogo das transportadoras
ENTREGA_NINJA = BaseCarrier(
    name="Entrega Ninja",
    constant=Decimal(0.3),
    min_height=10,
    max_height=200,
    min_width=6,
    max_width=140,
    delivery_days=6,
)

ENTREGA_KABUM = BaseCarrier(
    name="Entrega Kabum",
    constant=Decimal(0.2),
    min_height=5,
    max_height=140,
    min_width=13,
    max_width=125,
    delivery_days=4,
)

ALL_CARRIERS = [ENTREGA_NINJA, ENTREGA_KABUM]
