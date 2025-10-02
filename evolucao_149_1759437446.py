# Legado de Prometheus (Geração 1)\n# Meta: Otimizar o uso de bibliotecas e módulos para reduzir overhead e melhorar o desempenho do código Python.\n\n```
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer

@timer
def processar():
    print('código otimizado')