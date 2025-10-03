# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação e interpretação do código Python utilizando just-in-time (JIT) compilation ou profilers para identificar e melhorar os pontos mais lentos da aplicação.\n\nfrom functools import wraps
import time

def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'[{func.__name__}] took {end - start} seconds to execute.')
        return result
    return wrapper

@profile
def processar():
    print('código reescrito com profiling')

processar()