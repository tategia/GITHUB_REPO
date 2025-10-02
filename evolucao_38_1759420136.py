# Legado de Prometheus (Geração 1)\n# Meta: Aprimorar a utilização de just-in-time (JIT) compilation e caching para melhorar o desempenho dos programas Python.\n\n```
import functools
import time

@functools.lru_cache(maxsize=None)
def processar():
    start_time = time.time()
    print('código processado em {:.2f} segundos'.format(time.time() - start_time))
    print('código antigo')

processar()
```