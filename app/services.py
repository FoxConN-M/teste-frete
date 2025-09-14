from typing import List
from decimal import Decimal
from .models import QuoteRequest, QuoteResponse
from .carriers import ALL_CARRIERS, BaseCarrier
from decimal import Decimal, ROUND_HALF_UP
from typing import Optional

def get_quotes(req: QuoteRequest) -> List[QuoteResponse]:
    quotes = []
    for carrier in ALL_CARRIERS:
        q = _quote(req, carrier)
        if q:
            quotes.append(q)
    return quotes

def _quote(req: QuoteRequest, carrier: BaseCarrier) -> Optional[QuoteResponse]:
        TWOPLACES = Decimal("0.01")
        if not _is_eligible(req, carrier):
            return None
        # (weight * constant / 10) -> duas casas decimais
        raw = (Decimal(req.weight) * carrier.constant) / Decimal(10)
        amount = raw.quantize(TWOPLACES, rounding=ROUND_HALF_UP)
        return QuoteResponse.model_construct(
            nome=carrier.name,
            valor_frete=amount,
            prazo_dias=carrier.delivery_days,
        )

def _is_eligible(req: QuoteRequest, carrier: BaseCarrier) -> bool:
        h = req.dimension.height
        w = req.dimension.width
        return (
            carrier.min_height <= h <= carrier.max_height
            and carrier.min_width <= w <= carrier.max_width
            and req.weight > 0
        )
    

def to_serializable(item: QuoteResponse) -> dict:
    #converte decimal para float arredondado
    return {
        "nome": item.name,
        "valor_frete": float(Decimal(item.shipping_value)),
        "prazo_dias": item.delivery_days,
    }
