# Legado de Prometheus (Geração 1)\n# Meta: Aprender as técnicas de otimização do código Python para listas e dicionários, como o uso de `array.array`, `struct` e `numba`.\n\nimport numba

@numba.jit
def processar():
    print('código otimizado')

print('antes de chamar a função')
processar()
print('depois de chamar a função')