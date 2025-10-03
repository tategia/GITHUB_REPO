# Legado de Prometheus (Geração 1)\n# Meta: Aprender e implementar técnicas de otimização de código em Python para melhorar o desempenho de aplicativos e bibliotecas populares como NumPy, pandas e scikit-learn.\n\nfrom functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    
        value = func(*args, **kwargs)
        end_time = time.perf_counter() - start_time
        print(f"Executed {func.__name__!r} in {end_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def processar():
    print('código melhorado')