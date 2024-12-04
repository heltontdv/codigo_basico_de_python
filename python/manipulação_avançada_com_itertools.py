import itertools

numeros = [1, 2, 3]
perm = itertools.permutations(numeros)
comb = itertools.combinations(numeros, 2)

print("Permutações:", list(perm))
print("Combinações:", list(comb))
