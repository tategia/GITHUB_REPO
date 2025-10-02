# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação e execução de código Python utilizando just-in-time (JIT) compilation e caching para reduzir o tempo de resposta e melhorar o desempenho em aplicativos intensivos em CPU.\n\n```
import functools
import time

@functools.lru_cache(maxsize=None)
def processar():
    print('código otimizado')

@functools.wraps(processar)
def wrapper_processar(*args, **kwargs):
    start_time = time.time()
    result = processar(*args, **kwargs)
    end_time = time.time()
    print(f' Tempo de execução: {end_time - start_time} segundos')
    return result

processar()
```