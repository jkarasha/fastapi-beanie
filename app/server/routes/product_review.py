from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from ..models.product_review import ProductReview, UpdateProductReview

router = APIRouter()

@router.post("/", response_description="Add new product review")
async def add_product_review(review: ProductReview) -> dict:
    await review.create()
    return {"message": "Product review added successfully"}

@router.get("/{id}", response_description="Get a single product review")
async def get_review(id: PydanticObjectId) -> ProductReview:
    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.get("/", response_description="List all product reviews")
async def get_reviews() -> List[ProductReview]:
    reviews = await ProductReview.find_all().to_list()
    return reviews

@router.put("/{id}", response_description="Update a product review")
async def update_review_data(id: PydanticObjectId, req: UpdateProductReview) -> ProductReview:
    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
        
    update_data = req.model_dump(exclude_unset=True)
    
    await review.update({"$set": update_data})
    
    return await ProductReview.get(id)

@router.delete("/{id}", response_description="Delete a product review")
async def delete_review(id: PydanticObjectId) -> dict:
    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
        
    await review.delete()
    return {"message": "Review deleted successfully"}
