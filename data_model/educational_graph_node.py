from pydantic import BaseModel

class EducationalGraphNode(BaseModel):
    name: str
    description: str