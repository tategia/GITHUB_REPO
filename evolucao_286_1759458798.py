# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação e execução de código Python com just-in-time (JIT) compilation e técnicas de optimizations de nível baixo para aproveitar ao máximo as melhorias no desempenho do hardware recente.\n\n```
import numba

@numba.jit(nopython=True)
def processar():
    print('código otimizado')
```