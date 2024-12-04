import weakref

class Objeto:
    pass

obj = Objeto()
ref = weakref.ref(obj)

print(ref)  # Referência fraca
print(ref())  # Objeto ainda existe

del obj
print(ref())  # Objeto foi coletado pelo garbage collector
