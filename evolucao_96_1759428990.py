# Legado de Prometheus (Geração 1)\n# Meta: Optimizar funções Numba e Cython para melhorar o desempenho de códigos Python críticos em loops e matrizes.\n\nNo caso, como o processo é simplesmente uma impressão de texto, não há muito a ser feito para otimizar o desempenho do código. No entanto, se você quiser aplicar técnicas de otimização, aqui está um exemplo com Numba e Cython:

**Numba:**
```python
import numba

@numba.jit(nopython=True)
def processar():
    print('código numba')
```

**Cython:**
```cython
from cython import nopython

def processar():
    print("código Cython")

processar = nopython(processar)
```

Lembre-se de que essas abordagens podem não ser úteis para todos os casos, pois o código original era muito simples.