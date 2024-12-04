class Animal:
    def som(self):
        print("Som genérico")

class Cachorro(Animal):
    def som(self):
        print("Latido")

c = Cachorro()
c.som()
