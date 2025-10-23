"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Class name lowercased = collection name.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Inquiry(BaseModel):
    """
    Inquiries from the website contact form
    Collection name: "inquiry"
    """
    name: str = Field(..., min_length=2, description="Full name")
    email: EmailStr = Field(..., description="Contact email")
    type: Optional[str] = Field(None, description="Project type: Residential, Commercial, etc.")
    message: str = Field(..., min_length=10, description="Project details / message")

# Example schemas (kept for reference; unused by this app)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
