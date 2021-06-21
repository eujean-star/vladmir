import pandas as pd
from pandas.core.frame import DataFrame


def contagem_kmers(path:str) -> DataFrame:
    ''' 
    Return a relative count of kmers.

    Parameters:
    ==========
    Path: str
        Path of dataset.
    '''
    
    data = pd.read_csv(path, names=['kmers', 'con'], sep= ' ')
    data['con'] = data['con'].apply(lambda x : x/(data['con'].sum()))
    
    return data


def config_df(path:str, feature:int) -> DataFrame:
    '''
    Configure dataframe and add a label tha indicate if it's alzheimer patiente 
    or control group.

    Parameters:
    ===========
    Path: str
        it requieres the dataframe path.
    Feature: int
        if 1, indicate it's alzheimer patiente, else: control group.

    Returns:
    ========
    Dataframe. 
    
    '''    
   
    df = contagem_kmers(path)
    data = df.T.copy()
    data.rename(columns=data.loc['kmers'], inplace=True)
    data.drop('kmers', inplace=True)
    data['feature'] = feature
    data.fillna(0, inplace=True)
    return data

if __name__ == '__main__':

    print('configurando o grupo que apresenta a doença')
    data = config_df('../data/raw/al/SRR837438.kmers', 1)
    data = data.append(config_df('../data/raw/al/SRR837439.kmers', 1))
    data = data.append(config_df('../data/raw/al/SRR837440.kmers', 1))
    data = data.append(config_df('../data/raw/al/SRR837441.kmers', 1))
    data = data.append(config_df('../data/raw/al/SRR837442.kmers', 1))
    data = data.append(config_df('../data/raw/al/SRR837443.kmers', 1))
    data = data.append(config_df('../data/raw/al/SRR837444.kmers', 1))
    data = data.append(config_df('../data/raw/al/SRR837445.kmers', 1))
    data = data.append(config_df('../data/raw/al/SRR837446.kmers', 1))
    
    print('Adicionando os dados do grupo controle')
    data = data.append(config_df('../data/raw/con/SRR837471.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837472.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837473.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837474.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837475.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837476.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837477.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837478.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837479.kmers', 0))
    data = data.append(config_df('../data/raw/con/SRR837480.kmers', 0))

    data.fillna(0, inplace=True)
    data.to_csv('/home/jan/vladmir/data/processed/initial_data_processed.csv', index=False)