# Legado de Prometheus (Geração 1)\n# Meta: "Otimizar bibliotecas externas frequentemente usadas no seu código Python para melhorar o desempenho e reduzir a carga de memória."\n\n```
from cProfile import run
from pstats import SortKey

def processar():
    run("processar", sort='cumulative')
    print('código otimizado')
```