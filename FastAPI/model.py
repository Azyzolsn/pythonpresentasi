from typing import TypeVar, Optional
from pydantic import BaseModel, Field

T = TypeVar('T')

class Book(BaseModel):
    id: str
    title: str
    description: str


class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None
