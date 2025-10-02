# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a cacheamento em Python utilizando bibliotecas como `functools.lru_cache` ou `cachecontrol`.\n\n```
from functools import lru_cache

@lru_cache(maxsize=None)
def processar():
    print('código cacheado')
```