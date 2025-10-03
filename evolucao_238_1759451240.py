# Legado de Prometheus (Geração 1)\n# Meta: Optimizar a utilização do cache para reduzir a carga de memória e melhorar o desempenho!\n\n```
import functools

cache = {}

def memoized_processar():
    @functools.lru_cache(maxsize=None)
    def wrapper():
        if 'cached' not in cache:
            cache['cached'] = True
            print('código antigo')
        return 
    wrapper()
```