from pydantic import BaseModel
from typing import Optional

from data_model.educational_graph_node import EducationalGraphNode
from data_model.learning_object import LearningObject
from data_model.educational_path import EducationalPath

class UserCognitivePosition(BaseModel):
    formalPosition: EducationalGraphNode
    latestLearningObject: LearningObject
    historyOfEducation: EducationalPath