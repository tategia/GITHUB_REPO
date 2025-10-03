# Legado de Prometheus (Geração 1)\n# Meta: "Optimar o uso do cache em Python utilizando bibliotecas como functools.lru_cache ou joblib para melhorar o desempenho das funções computacionalmente intensivas."\n\n```
from functools import lru_cache

@lru_cache(maxsize=None)
def processar():
    print('código otimizado')
```