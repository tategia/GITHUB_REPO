# Legado de Prometheus (Geração 1)\n# Meta: Aprender a utilizar just-in-time compiling (compilando à medida) em Python utilizando tecnologias como PyPy ou Numba.\n\nPara melhorar a performance do código anterior, podemos utilizar o Numba, que é uma biblioteca de compilador just-in-time (JIT) para Python. Aqui está o código rewritten:
```python
import numba

@numba.jit(nopython=True)
def processar():
    print('código novo e mais rápido!')
```
O `@numba.jit` é uma decorator que permite ao Numba compilar a função em tempo de execução. O parâmetro `nopython=True` indica que a função não deve ter acesso às funções dinâmicas do Python, o que melhora a performance.

Lembre-se de que para que isso funcione, você precisará instalar o Numba com pip: `pip install numba`.