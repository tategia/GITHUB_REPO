# Legado de Prometheus (Geração 1)\n# Meta: Melhorar o uso de just-in-time (JIT) compiladores em Python para aumentar o desempenho dos aplicativos.\n\nfrom functools import wraps
import timeit

def compile_jit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    code = compile(wrapper.__code__, '<string>', 'exec')
    return types.FunctionType(code)

processar = compile_jit(lambda: print('código compilado'))