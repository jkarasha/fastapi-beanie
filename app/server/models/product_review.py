from datetime import datetime
from typing import Optional
from beanie import Document
from pydantic import BaseModel, Field


class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.utcnow()

    class Settings:
        name = "product_review"

    class Config:
        schema_extra = [
            {
                "name": "John Doe",
                "product": "Coffee Maker", 
                "rating": 4.5,
                "review": "Great coffee maker, makes perfect coffee every time!",
                "date": datetime.utcnow()
            }
        ]

class UpdateProductReview(BaseModel):
    name: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "product": "Coffee Maker",
                "rating": 4.5,
                "review": "Updated review: Still loving this coffee maker!",
                "date": datetime.utcnow()
            }
        }

