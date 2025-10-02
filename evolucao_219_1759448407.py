# Legado de Prometheus (Geração 1)\n# Meta: Otimizar o uso de memória em Python mediante a implementação eficiente do garbage collection e a minimização da criação de objetos desnecessários.\n\n```
import gc
gc.collect()

def processar():
    try:
        print('código otimizado')
    finally:
        del processar
```