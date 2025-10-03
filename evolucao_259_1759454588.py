# Legado de Prometheus (Geração 1)\n# Meta: Aprender e implementar técnicas de otimização para trabalhar com dados grandes em Python, utilizando bibliotecas como Pandas e NumPy, para melhorar o desempenho de análises e processamentos de grande escala.\n\n```
import pandas as pd
import numpy as np

def processar(data: pd.DataFrame) -> None:
    data = data.drop_duplicates()  # Remova linhas duplicadas (se houver)
    data['column_name'] = data['column_name'].apply(lambda x: np.nan if x < 0 else x)  # Trate valores negativos
    data = data.loc[data['column_name'].notna()]  # Filtragem de linhas com NaN
    print('código otimizado')
```