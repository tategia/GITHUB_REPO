# Legado de Prometheus (Geração 1)\n# Meta: Melhorar o uso de just-in-time compilation (compilação just-in-time) e caching em Python para otimizar o desempenho dos programas.\n\n```
import functools
import time

@functools.lru_cache(maxsize=None)
def processar():
    start_time = time.time()
    print('processando...')
    result = 'código otimizado'
    end_time = time.time()
    print(f'Tempo de execução: {end_time - start_time} segundos')
    return result
```