# Legado de Prometheus (Geração 1)\n# Meta: "Melhorar o uso do just-in-time (JIT) e caching para acelerar a execução de código em Python".\n\n```
import functools
import time

@functools.lru_cache(maxsize=None)
def processar():
    start_time = time.time()
    print('código antigo')
    end_time = time.time()
    execution_time = end_time - start_time
    print(f'Execução tomou {execution_time} segundos.')
```