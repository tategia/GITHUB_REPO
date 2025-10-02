# Legado de Prometheus (Geração 1)\n# Meta: Aprimorar a compilação just-in-time (JIT) em Python.\n\nfrom typing import Callable

jit_enabled: bool = True  # Habilita ou desabilita a compilação just-in-time
compiled_function: Callable[[], None] | None = None

def processar() -> None:
    global compiled_function, jit_enabled
    
    if not jit_enabled or compiled_function is None:
        def compiled_processar():
            print('código compilado')
        
        compiled_function = compiled_processar
    else:
        compiled_function()
    
    if __name__ == '__main__':
        processar()