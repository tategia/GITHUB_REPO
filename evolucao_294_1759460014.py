# Legado de Prometheus (Geração 1)\n# Meta: Aprimorar a compilação just-in-time (JIT) para Python.\n\n```
import timeit
import functools

jit_cache = {}

def jit(func):
    def wrapper(*args, **kwargs):
        key = (func.__name__, tuple(args), frozenset(kwargs.items()))
        if key in jit_cache:
            return jit_cache[key]
        
        result = func(*args, **kwargs)
        jit_cache[key] = result
        return result
    
    return functools.update_wrapper(wrapper, func)

@jit
def processar():
    print('código compilado')

processar()
```