# Legado de Prometheus (Geração 1)\n# Meta: Aprimorar a compreensão de cálculo de tempo de execução e uso eficaz da biblioteca `cProfile` em Python para melhorar o desempenho do código.\n\n```
import cProfile
import pstats

def processar():
    print('código aprimorado')

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    processar()

    profiler.disable()
    ps = pstats.Stats(profiler).sort_stats('cumulative')
    ps.print_stats()
```