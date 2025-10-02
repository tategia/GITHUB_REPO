# Legado de Prometheus (Geração 1)\n# Meta: Aprender e implementar técnicas de profiling e benchmarking para identificar e otimizar os pontos críticos do código Python.\n\n```
import timeit
import cProfile

def processar():
    for i in range(10000):
        print('novo processo')

print('Executando o método...')
t = timeit.Timer("processar()", globals())
result = t.timeit(number=1)
print(f'Tempo de execução: {result} segundos')

cProfile.run('processar()')
```