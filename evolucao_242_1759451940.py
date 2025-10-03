# Legado de Prometheus (Geração 1)\n# Meta: Aprimorar a compreensão do perfil de desempenho da aplicação para identificar e optimizar as partes críticas do código Python.\n\n```
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # Inicio do tempo de execução
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # Fim do tempo de execução
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def processar():
    print('Novo código processado com timer')

processar()
```