class MinhaExcecao(Exception):
    pass

try:
    raise MinhaExcecao("Algo deu errado!")
except MinhaExcecao as e:
    print(e)
