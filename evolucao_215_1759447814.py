# Legado de Prometheus (Geração 1)\n# Meta: Aprender a utilizar profilers e ferramentas de análise do desempenho para identificar e otimizar os trechos de código que mais afetam o rendimento.\n\n```
import cProfile
from pstats import SortKey

def processar():
    cProfile.runctx("print('código antigo')", globals(), locals())

processar()
p = cProfile.Profile()
p.enable()
processar()
p.disable()

ps = p.getstats(sort=SortKey.CUMULATIVE)
for ps in ps:
    print(ps)