# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compreensão do profiling para identificar as partes do código que mais afetam o desempenho e priorizar esforços para melhorá-las.\n\n```
import time
import cProfile
import pstats

def processar():
    start_time = time.time()
    print('Início da execução')
    for i in range(1000000):
        pass  # Simula trabalho
    end_time = time.time()
    print(f'Tempo de execução: {end_time - start_time} segundos')

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    processar()
    profiler.disable()
    ps = pstats.Stats(profiler).sort_stats('cumulative')
    ps.print_stats()
```