from modelos.base import BaseModel
from sklearn.ensemble import RandomForestClassifier

class VladRan(BaseModel):

    def __init__(self) -> RandomForestClassifier:
        self.model = RandomForestClassifier()
        

    