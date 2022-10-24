from typing import Iterable
from pydantic import BaseModel

class EducationalPathNode(BaseModel):
    name: str
    description: str