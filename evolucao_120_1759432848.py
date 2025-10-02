# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação just-in-time (JIT) para obter melhorias significativas no desempenho do código Python.\n\n```
import timeit
from functools import lru_cache

@lru_cache(maxsize=None)
def processar():
    print('código otimizado')

print(timeit.timeit(processar, number=10000))
```