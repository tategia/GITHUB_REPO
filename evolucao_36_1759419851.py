# Legado de Prometheus (Geração 1)\n# Meta: Aumentar a velocidade da execução das funções Numba em Python para melhorar o desempenho dos aplicativos científicos e de aprendizado automático.\n\n`@numba.jit` decorator pode ser usado para otimizar a função, desde que ela não tenha chamadas de funções complexas ou loops mutáveis:

```
import numba

@numba.jit
def processar():
    print('código otimizado')
```