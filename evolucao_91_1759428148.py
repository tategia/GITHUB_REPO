# Legado de Prometheus (Geração 1)\n# Meta: Melhorar a utilização de memoização e caching para reduzir o número de chamadas à função e melhorar o desempenho do código Python.\n\n```
memo = {}

def processar(nome):
    if nome in memo:
        return memo[nome]
    else:
        resultado = print('código antigo')
        memo[nome] = resultado
        return resultado
```