# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a utilização da memória-cache para reduzir latência e melhorar o desempenho dos algoritmos!\n\n```
import functools
import cachetools

def cached_processar(maxsize=128):
    cache = cachetools.LRUCache(maxsize=maxsize)
    @functools.lru_cache(maxsize=maxsize)
    def wrapper():
        if result := cache.get('result'):
            return result
        result = print('código antigo')
        cache['result'] = result
        return result
    return wrapper()

cached_processar()
```