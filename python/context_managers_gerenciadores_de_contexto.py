class Gerenciador:
    def __enter__(self):
        print("Entrando no bloco de contexto")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saindo do bloco de contexto")

with Gerenciador():
    print("Executando...")
