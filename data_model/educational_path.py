from pydantic import BaseModel
from typing import Optional, List
from data_model.educational_path_node import EducationalPathNode

class EducationalPath(BaseModel):
    start: EducationalPathNode
    end: EducationalPathNode
    stations: Optional[List[EducationalPathNode]]