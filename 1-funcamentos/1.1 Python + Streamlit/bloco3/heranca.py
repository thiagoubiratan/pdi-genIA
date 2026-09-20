# classe pai
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "..."


# classes filhas - herdam de Animal
class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} diz: Au au!"


class Gato(Animal):
    def falar(self):
        return f"{self.nome} diz: Miau!"


# Criando objetos
cachorro = Cachorro("Rex")
gato = Gato("Mimi")

print(cachorro.falar())  # Rex diz: Au au!
print(gato.falar())  # MIni diz: Miaßu!
