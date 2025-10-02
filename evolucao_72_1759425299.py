# Legado de Prometheus (Geração 1)\n# Meta: Melhorar o desempenho da memória na aplicação Python.\n\n```
import functools

def memorize(func):
    cache = dict()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

@memorize
def processar():
    print('código melhorado')
```