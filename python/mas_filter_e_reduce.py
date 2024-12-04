from functools import reduce

numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x ** 2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
soma = reduce(lambda x, y: x + y, numeros)

print(quadrados, pares, soma)
