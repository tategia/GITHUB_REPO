# Legado de Prometheus (Geração 1)\n# Meta: Aprender e implementar técnicas de caching para melhorar o desempenho dos algoritmos em Python!\n\n```
import functools

cache = {}

@functools.lru_cache(maxsize=None)
def processar():
    if 'código antigo' in cache:
        return cache['código antigo']
    print('código antigo')
    result = 'código antigo'
    cache['código antigo'] = result
    return result
```