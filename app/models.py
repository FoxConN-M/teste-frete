from __future__ import annotations
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class DimentionIn(BaseModel):
    height: int = Field(..., ge=0, alias="altura", description="Height in cm")
    widht: int = Field(..., ge=0, alias="largura", description="Widht in cm")

class QuoteRequest(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    dimention: DimentionIn = Field(..., alias="dimensao")
    weight: int = Field(..., alias="peso", gt=0, description="Weight in grams")

class QuoteResponse(BaseModel):
    name: str = Field(alias="nome")
    shipping_value: Decimal = Field(alias="valor_frete")
    delivery_days: int = Field(alias="prazo_dias")
