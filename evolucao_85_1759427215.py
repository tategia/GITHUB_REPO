# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a utilização do just-in-time (JIT) e da compilação estática em Python para reduzir o tempo de execução e melhorar o desempenho dos programas.\n\n```
import functools
import time

@functools.lru_cache(maxsize=None)
def processar():
    print('código compilado')
    return time.time()

processar()
```