# Legado de Prometheus (Geração 1)\n# Meta: Aprimorar a compreensão e utilização do Just-In-Time (JIT) compilador em Python para melhorar o desempenho dos scripts.\n\nfrom llvmlite import ir
import numba

@numba.jit
def processar():
    print('código JIT compilado')

# Utilize o módulo JIT do Numba para compilar o código da função
processar()