# Legado de Prometheus (Geração 1)\n# Meta: "Melhorar a execução de loops e list comprehensions em Python para alcançar melhorias significativas no desempenho do código".\n\n```
import timeit

old_function = lambda: print('código antigo')

new_function = lambda: [print(i) for i in range(1000)]

if __name__ == "__main__":
    old_time = timeit.timeit(old_function, number=1000)
    new_time = timeit.timeit(new_function, number=1000)

    print(f"Tempo antigo: {old_time} segundos")
    print(f"Tempo novo: {new_time} segundos")
```