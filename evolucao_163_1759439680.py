# Legado de Prometheus (Geração 1)\n# Meta: Aprimorar a compreensão do perfil de memória e cache para melhorar o desempenho em cenários de baixa memória ou CPU.\n\n```
import functools
import cachetools

@functools.lru_cache(maxsize=None)
@cachetools.cached(ttl=60)  # cache for 1 minute
def processar():
    print('código processado')
```