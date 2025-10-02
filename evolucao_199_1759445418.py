# Legado de Prometheus (Geração 1)\n# Meta: Optimizar funções de alto uso de CPU para melhorar o desempenho do código Python em aplicativos que requerem processamento intensivo.\n\n```
import concurrent.futures
import time

def processar():
    for _ in range(1000000):
        pass  # Simule o processamento intensivo aqui

if __name__ == '__main__':
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(processar) for _ in range(4)]
        for future in concurrent.futures.as_completed(futures):
            future.result()
    end_time = time.time()
    print(f"Processamento concluído em {end_time - start_time:.2f} segundos")
```