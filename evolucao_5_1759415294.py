# Legado de Prometheus (Geração 1)\n# Meta: Melhorar o uso do Just-In-Time (JIT) compilador para aplicativos Python, como o PyPy e Numba, para obter melhorias significativas no desempenho em loops intensivos e operações computacionais complexas.\n\n```
import numba

@numba.jit
def processar():
    print('Código compilado com JIT!')
```