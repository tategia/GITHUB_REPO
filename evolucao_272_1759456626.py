# Legado de Prometheus (Geração 1)\n# Meta: Optimizar a implementação do método `map` para trabalhar com iteráveis muito grandes em Python.\n\n```
import concurrent.futures

def processar(iteracao):
    for item in iteracao:
        # implementação do processo a ser feito
        pass

def processar_iteravel(iterable, num_workers=None):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_workers) as executor:
        list(executor.map(processar, iterable))

processar_iteravel(range(1000000))  # exemplo de uso: processar iterável com um milhão de elementos
```