# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação e execução do código Python utilizando Just-In-Time (JIT) compiladores ou frameworks como Numba, Cython ou PyPy.\n\nPara melhorar a compilação e execução do código Python utilizando Numba, você pode substituir a função `print` pela função `numba.print_`, como segue:
```
import numba

@numba.jit
def processar():
    numba.print_('código novo')
```