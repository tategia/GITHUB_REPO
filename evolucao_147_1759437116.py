# Legado de Prometheus (Geração 1)\n# Meta: Aprender e implementar técnicas de optimização de código em Python para melhorar o desempenho de aplicativos e scripts, como: profiling, caching, memoization, parallel processing, just-in-time compilation, entre outras.\n\n```
import cProfile
from functools import lru_cache

@lru_cache(maxsize=None)
def processar():
    print('Código otimizado!')
```