# Legado de Prometheus (Geração 1)\n# Meta: Aprender sobre Just-In-Time (JIT) compilation para Python.\n\n```
import timeit

def processar():
    print('Código compilado com Just-In-Time')

# Compilando a função
for _ in range(100):
    processar()

print("Tempo de execução:")
exec_time = timeit.timeit(processar, number=1000)
print(f"{exec_time:.4f} segundos")
```