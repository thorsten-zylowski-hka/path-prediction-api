from pydantic import BaseModel
from typing import Optional

class UserGoal(BaseModel):
    goalDescription: str # TODO