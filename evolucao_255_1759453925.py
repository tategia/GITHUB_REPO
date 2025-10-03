# Legado de Prometheus (Geração 1)\n# Meta: Aprender a utilizar just-in-time (JIT) compiladores e técnicas de compilação estática para melhorar o desempenho do código Python.\n\n```
import numba

@numba.jit(nopython=True)
def processar():
    print('código otimizado')
```