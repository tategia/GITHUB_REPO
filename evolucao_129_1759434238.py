# Legado de Prometheus (Geração 1)\n# Meta: Aprender a utilizar just-in-time (JIT) compilation e caching para melhorar o desempenho do código Python em tempo de execução.\n\n```
import functools

@functools.lru_cache(maxsize=None)
def processar():
    print('código compilado')
```