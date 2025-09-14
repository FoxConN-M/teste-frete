from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal

@dataclass(frozen=True)

class BaseCarrier:
    name: str
    constant: Decimal
    min_height: int 
    max_height: int
    min_width: int
    max_width: int
    delivery_days: int

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
