from modelos.base import BaseModel
from sklearn.ensemble import ExtraTreesClassifier

class VladEx(BaseModel):
    def __init__(self)-> ExtraTreesClassifier:
        self.model = ExtraTreesClassifier()
