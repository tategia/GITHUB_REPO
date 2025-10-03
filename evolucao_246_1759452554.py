# Legado de Prometheus (Geração 1)\n# Meta: Melhorar o uso de decorators e caching para reduzir a complexidade e melhorar a eficiência do código Python.\n\n```
import time
from functools import wraps

def log_tempo(mensagem):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fim = time.time()
            print(f'[{mensagem}] {func.__name__} levou {fim - inicio} segundos para executar.')
            return resultado
        return wrapper
    return decorator

@log_tempo('processamento')
def processar():
    time.sleep(2)  # Simulando tempo de processamento
    print('código antigo')

processar()
```