# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a utilização de bibliotecas como NumPy e Pandas para processamento de dados em Python.\n\nfrom typing import List
import pandas as pd
import numpy as np

def processar(data: List[pd.DataFrame]) -> None:
    for df in data:
        df['nova_coluna'] = np.sum(df[['coluna1', 'coluna2']])
    print('código melhorado')