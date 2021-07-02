from sklearn.metrics import classification_report
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.base import BaseEstimator

class BaseModel:
    def __init__(self, model:BaseEstimator=RandomTreesEmbedding) -> None:
        self.model = model

    def fit(self, X, y) -> None:
        self.model.fit(X, y)
    
    def pred(self, X):
        return self.model.predict(X)
    
    def validation(self, X_test, y_test):
        y_pred = self.pred(X_test)
        return classification_report(y_test, y_pred)