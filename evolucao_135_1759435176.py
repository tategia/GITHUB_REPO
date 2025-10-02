# Legado de Prometheus (Geração 1)\n# Meta: "Melhorar o uso da just-in-time (JIT) compilation em projetos Python para reduzir overhead e melhorar o desempenho das aplicações."\n\n```
import functools
import time

@functools.lru_cache(maxsize=None)
def processar():
    start_time = time.time()
    print('processamento em andamento...')
    print('código processado')
    end_time = time.time()
    print(f'Tempo de execução: {end_time - start_time} segundos')
```