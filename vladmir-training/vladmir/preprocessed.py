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
    data = df.T
    data.rename(columns=data.loc['kmers'], inplace=True)
    data.drop('kmers', inplace=True)
    data['feature'] = feature
    data.fillna(0, inplace=True)
    return data


if __name__ == '__main__':
    
    '''Abrindo o df contendo os SRR'''
    df_metadata = pd.read_csv('data/SraRunTable.txt', sep=',')
    
    ''' Esse df_final é onde os arquivos *.kmer vão ser guardados depois de serem processados'''
    df_final = pd.DataFrame() 
    '''Onde a iteração acontece. O método iterrows retorna pra gente tanto o índice quanto o conteudo do mesmo
    sendo:
    r: Índice
    row: A linha com o conteudo de todas as colunas'''
    for r, row in df_metadata.iterrows():
        '''row.Run acessa o SRR na coluna Run.'''
        srr = row.Run    
        ''' O objeto srr guarda o valor (código de acesso do arquivo que ta na pasta data/raw)
        e utilizei essa váriavel para iterar sobre os arquivos na pasta'''
        
        '''Como a coluna Group indica se é Grupo de controle ou não dá pra usar estrutura de condição pra setar o parametro
        feature da função condif_df'''
        if 'alzheimer' in row.Group:
            '''Note que esse feat é o valor do paremetro feature caso a palavra alzheime estiver na coluna Group'''
            feat = 1
            df_final = df_final.append(config_df(f'data/raw/{srr}.kmer', feature = feat))
        else:
            '''Caso contrário, 0. Isso indica que é do grupo controle '''
            feat = 0
            df_final = df_final.append(config_df(f'data/raw/{srr}.kmer', feature = feat))
    '''
    Como o modelo precisa necessariamente que o valor das colunas seja numeros, os valores nulos (Missing value)
    serão preenchidos com 0
    '''
    df_final.fillna(0, inplace=True)        
    '''Salvo  o dataframe formatado na pasta data/processed'''
    df_final.to_csv('data/processed/dataframe_processed.csv', index=False)


    #Esse script precisa ser rodado na pasta do projeto. 
    # Se for executado dentro de outra pasta vai dar erro por conta do path