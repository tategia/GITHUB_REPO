# Legado de Prometheus (Geração 1)\n# Meta: Aprender a otimizar código Python com técnicas como profiling, utilização de bibliotecas eficientes e aplicação do conceito de caching para melhorar o desempenho dos programas.\n\n```
import cProfile
from functools import lru_cache

@lru_cache(maxsize=None)
def processar():
    print('Código otimizado')
```