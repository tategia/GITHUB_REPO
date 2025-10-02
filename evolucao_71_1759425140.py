# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a compilação just-in-time (JIT) para obter melhorias no desempenho e uso eficiente da memória em aplicativos Python críticos de desempenho.\n\n```
import functools

@functools.lru_cache(maxsize=None)
def processar():
    print('código otimizado')
```