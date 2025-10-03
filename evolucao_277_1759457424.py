# Legado de Prometheus (Geração 1)\n# Meta: Melhorar o uso de memoization e caching em Python para reduzir o número de chamadas ao sistema e melhorar o desempenho das funções computacionais intensivas.\n\n```
import functools

@functools.lru_cache(maxsize=None)
def processar():
    if not hasattr(processar, 'resultado'):
        print('código antigo')
        setattr(processar, 'resultado', True)
    else:
        print('Código processado previamente!')
```