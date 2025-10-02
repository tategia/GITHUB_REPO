# Legado de Prometheus (Geração 1)\n# Meta: "Implementar caching eficaz para reduzir a quantidade de chamadas à memória e ao disco rígido em aplicativos Python".\n\n```
import functools
from cachetools import cached, TTLCache

_cache = TTLCache(maxsize=100, ttl=60)  # cache with a maximum size of 100 and a time-to-live of 1 minute

@cached(_cache)
def processar():
    print('código novo')
```