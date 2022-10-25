from pydantic import BaseModel

class LearningObject(BaseModel):
    name: str
    description: str