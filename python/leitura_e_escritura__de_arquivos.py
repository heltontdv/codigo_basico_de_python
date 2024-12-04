with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Escrevendo no arquivo!")

with open("arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
