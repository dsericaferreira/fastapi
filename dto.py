from pydantic import BaseModel

# DTO
class FibonacciRequest(BaseModel):
    payload: int