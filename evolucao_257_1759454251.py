# Legado de Prometheus (Geração 1)\n# Meta: "Otimizar a utilização do cache para reduzir a quantidade de requisições à base de dados em aplicativos web"\n\n```
from functools import lru_cache

@lru_cache(maxsize=None)
def processar():
    print('Código otimizado')
```