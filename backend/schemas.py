from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int

    model_config = {
        "from_attributes": True
    }

class ProductResponse(ProductCreate):
    id: int

    model_config = {
        "from_attributes": True
    }

class ChatRequest(BaseModel):
    message: str

    model_config = {
        "from_attributes": True
    }
