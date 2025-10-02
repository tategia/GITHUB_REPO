# Legado de Prometheus (Geração 1)\n# Meta: **Aprender e implementar técnicas de just-in-time compilation (JIT) para melhorar o desempenho do código Python**\n\n```
import functools
from typing import Callable

def processar() -> None:
    _processar = functools.partial(print, 'código otimizado')
    _processar()

_processar = functools.update_wrapper(processar, _processar)

__original_processar = globals().get('processar', None)
if __original_processar is not None:
    del globals()['processar']
del processar
globals()['processar'] = _processar
```