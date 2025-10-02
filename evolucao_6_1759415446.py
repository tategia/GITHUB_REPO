# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a utilização do Just-In-Time (JIT) e caching em Python para melhorar o desempenho dos programas.\n\n```
import functools
import time

@functools.lru_cache(maxsize=None)
def processar():
    return print('Código Processado com Cache!')

if __name__ == "__main__":
    start = time.time()
    for _ in range(100):
        processar()
    end = time.time()
    print(f'Tempo total: {end - start} segundos')
```