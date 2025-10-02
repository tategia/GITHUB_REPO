# Legado de Prometheus (Geração 1)\n# Meta: Melhorar o uso de just-in-time compiladores e caching para reduzir a latência e melhorar o desempenho em aplicativos Python que dependem fortemente da execução dinâmica do código.\n\nPara melhorar o desempenho, você pode utilizar um just-in-time (JIT) compilador como é utilizado pelo framework Numba. Aqui está o exemplo:

```
import numba

@numba.jit(nopython=True)
def processar():
    print('código otimizado')
```