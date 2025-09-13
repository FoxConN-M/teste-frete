from typing import List
from decimal import Decimal
from .models import QuoteRequest, QuoteResponse
from .carriers import ALL_CARRIERS

def get_quotes(req: QuoteRequest) -> List[QuoteResponse]:
    quotes: List[QuoteResponse] = []
    for carrier in ALL_CARRIERS:
        q = carrier.quote(req)
        if q:
            quotes.append(q)
    return quotes

def to_serializable(item: QuoteResponse) -> dict:
    #converte decimal para float arredondado
    return {
        "nome": item.name,
        "valor_frete": float(Decimal(item.shipping_value)),
        "prazo_dias": item.delivery_days,
    }
