# Legado de Prometheus (Geração 1)\n# Meta: Optimizar algoritmos para leitura e escrita de arquivos em Python utilizando bibliotecas como NumPy e Pandas.\n\n```
import numpy as np
import pandas as pd

def processar():
    data = pd.read_csv('arquivo.csv')
    np.save('saida.npy', data)
```