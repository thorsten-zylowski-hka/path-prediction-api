from pydantic import BaseModel
from typing import Optional
from data_model.user_cognitive_position import UserCognitivePosition
from data_model.user_goal import UserGoal
from data_model.user_requirements import UserRequirements

class PathPredictionRequest(BaseModel):
    cognitive_position: UserCognitivePosition
    goal: UserGoal
    requirements: UserRequirements