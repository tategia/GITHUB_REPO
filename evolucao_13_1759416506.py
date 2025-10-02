# Legado de Prometheus (Geração 1)\n# Meta: Otimizar a utilização de bibliotecas e módulos em Python para melhorar o desempenho dos aplicativos.\n\n```
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        logger.info(f'{func.__name__} took {end_time - start_time}')
        return result
    return wrapper

@timing
def processar():
    print('Código otimizado')
```