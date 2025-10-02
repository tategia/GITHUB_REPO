# Legado de Prometheus (Geração 1)\n# Meta: Melhorar o uso de caching para reduzir a carga de trabalho e melhorar o desempenho dos aplicativos em Python.\n\n```
import functools
from functools import lru_cache

@lru_cache(maxsize=None)
def processar():
    print('Código reescrito com caching')
```