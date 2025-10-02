# Legado de Prometheus (Geração 1)\n# Meta: Aprender sobre profilers e análise de perfomance para identificar áreas de melhoria no código Python e otimizá-las efetivamente.\n\n```
import cProfile
import pstats

def processar():
    profile = cProfile.Profile()
    profile.enable()
    print('código processando...')
    profile.disable()
    ps = pstats.Stats(profile)
    ps.sort_stats('cumulative')
    ps.print_stats()
```