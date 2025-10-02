# Legado de Prometheus (Geração 1)\n# Meta: Aprender e implementar técnicas de optimization para bibliotecas populares em Python como NumPy, pandas e scikit-learn.\n\n`from functools import wraps`

`def timer(func):`

`    @wraps(func)`

`    def wrapper(*args, **kwargs):`

`        start_time = time.time()`

`        result = func(*args, **kwargs)`

`        end_time = time.time()`

`        print(f'Função {func.__name__} demorou {end_time - start_time:.2f} segundos para ser executada.')`

`        return result`

`@timer`

`def processar():`

`    print('código reescrito')`