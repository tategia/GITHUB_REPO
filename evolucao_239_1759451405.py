# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a cacheamento e a utilização de bibliotecas como Numba ou Cython para aproveitar ao máximo o desempenho do código Python.\n\nFrom the meta, I understand that you want to improve the performance of your code by using Numba or Cython. Here's an example of how you can use Numba to compile your `processar` function:

```
import numba

@numba.jit
def processar():
    print('código melhorado')
```

In this example, the `@numba.jit` decorator tells Numba to compile the `processar` function into machine code, which can be executed more efficiently than regular Python code.