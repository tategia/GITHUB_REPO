# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação e otimização do bytecode Python utilizando `py_compile` e `bytecodeoptimizers`.\n\n```
import py_compile
import bytecodeoptimizers

@bytecodeoptimizers.optimize_bytecode
def processar():
    print('código otimizado')
```