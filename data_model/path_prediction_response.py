from pydantic import BaseModel
from typing import List

from data_model.educational_path import EducationalPath

class PathPredictionResponse(BaseModel):
    educationals_paths: List[EducationalPath]