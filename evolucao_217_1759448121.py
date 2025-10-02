# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação e interpretação do código Python em tempo real para aumentar a velocidade de execução e reduzir o overhead de chamadas de função.\n\n```
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execução do código: {end_time - start_time} segundos')
        return result
    return wrapper

@timer
def processar():
    print('Código processado!')

processar()