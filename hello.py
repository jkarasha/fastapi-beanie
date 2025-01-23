from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

class Item(Document):
    name: str
    description: str

    class Settings:
        name = "items"  # Collection name

        
async def main():
    # Connect to MongoDB
    client = AsyncIOMotorClient("mongodb://localhost:27017/")
    database = client["productreviews"]

    # Initialize Beanie
    await init_beanie(database=database, document_models=[Item])

    # Define collation
    collation = {"locale": "en", "strength": 3}  # Case-insensitive comparison

    # Query with collation
    items = await Item.find({"name": "john"}).to_list()
    for item in items:
        print(item)

    # Sort with collation
    sorted_items = await Item.find().sort("name").to_list()
    for item in sorted_items:
        print(item)
    #
    # Create a new item
    new_item = Item(name="Laptop", description="A high-performance laptop")

    # Insert the item into the collection
    await new_item.insert()

    print("Item inserted successfully!")


# Run the application
import asyncio
asyncio.run(main())

