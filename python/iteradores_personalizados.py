class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.contador = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        raise StopIteration

for num in Contador(5):
    print(num)
