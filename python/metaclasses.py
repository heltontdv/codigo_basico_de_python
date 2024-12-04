class MinhaMeta(type):
    def __new__(cls, name, bases, dct):
        dct['criado_por'] = "MetaProgramação"
        return super().__new__(cls, name, bases, dct)

class MinhaClasse(metaclass=MinhaMeta):
    pass

print(MinhaClasse.criado_por)
