from pydantic import BaseModel
from typing import Optional
from data_model.user_cognitive_position import UserCognitivePosition
from data_model.user_goal import UserGoal

class PathPredictionRequest(BaseModel):
    cognitive_position: UserCognitivePosition
    goal: UserGoal
    requirements: dict # TODO