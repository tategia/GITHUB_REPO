# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação e interpretação do código Python utilizando just-in-time (JIT) compilation e caching para reduzir o tempo de execução dos programas.\n\n```
import functools
import time

@functools.lru_cache(maxsize=None)
def processar():
    print('novo código compilado!')
    return time.sleep(1)  # para demonstrar que o tempo de execução diminuiu
```