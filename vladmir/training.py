from sklearn.model_selection import train_test_split
from modelos import VladEx
from modelos import VladRan
from pandas.core.frame import DataFrame
import pandas as pd

def main(path:str) -> DataFrame:
    '''
    Applies a machine learning model

    Parameter:
    ---------
    Path: str
        DataFrame path to be processed
    
    Returns:
    -------
    Dataframe
        A file containing classification report
    '''
    
    data = pd.read_csv(path)
    X = data.drop(['feature'], axis=1)
    y = data['feature']
    X_train, X_test, y_train, y_test = train_test_split(X,y)

    model = VladRan()
    model.fit(X_train, y_train)

    y_pred = model.pred(X_test)
    report = model.validation(y_pred, y_test)
    print(report)
    return report

if __name__ == '__main__':
    model = main('data/processed/initial_data_processed.csv')

