import motor.motor_asyncio
from beanie import init_beanie

from .models.product_review import ProductReview

async def init_db():
    # Create Motor client
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/productreviews"
    )

    # Initialize beanie with the Product Review document class
    await init_beanie(
        database=client.product_reviews_db,
        document_models=[ProductReview]
    )
