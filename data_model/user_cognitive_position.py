from pydantic import BaseModel
from typing import Optional

class UserCognitivePosition(BaseModel):
    currentState: str