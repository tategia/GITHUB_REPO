# Legado de Prometheus (Geração 1)\n# Meta: Aprimorar o uso do just-in-time (JIT) compilador em Python para melhorar o desempenho de aplicativos intensivos em computação.\n\n```
import numba

@numba.jit(nopython=True)
def processar():
    print('código aprimorado com JIT')
```