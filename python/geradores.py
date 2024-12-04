def gerador():
    for i in range(5):
        yield i

for valor in gerador():
    print(valor)
