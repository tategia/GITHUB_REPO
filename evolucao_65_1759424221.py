# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação e interpretação do código Python utilizando Just-In-Time (JIT) compilation para obter um desempenho mais rápido.\n\n```
import numba

@numba.jit(nopython=True)
def processar():
    print('código compilado com JIT')
```