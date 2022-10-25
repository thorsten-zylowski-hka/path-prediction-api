from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class GeoJsonPoint(BaseModel):
    coordinates: List[float]
    type: str

class Location(BaseModel):
    name: str
    lat_lon: GeoJsonPoint
    radius: float

class OptimizationCriteria(str, Enum):
    minimum_duration = "minimumDuration"
    costs = "minimumCosts"
    theory_oriented = "theoryOriented"
    practice_oriented = "practiceOriented"


class UserRequirements(BaseModel):
    optimization_criteria: List[OptimizationCriteria] # e.g. ['minimumDuration', 'practiceOriented']
    location: Optional[Location]