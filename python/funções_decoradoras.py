def decorador(funcao):
    def wrapper():
        print("Antes da função")
        funcao()
        print("Depois da função")
    return wrapper

@decorador
def mensagem():
    print("Função executada!")

mensagem()
