# definindo uma classe
class Pessoa:

    # construtor - executado ao criar um objeto
    def __init__(self, nome, idade):
        self.nome = nome  # atributo da classe
        self.idade = idade  # atributo da classe

    # método da classe
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

    # método que modifia um atributo
    def aniversario(self):
        self.idade += 1
        return f"Feliz anivesário {self.nome}! Agora tem {self.idade} anos"


# criando objetos
pessoa1 = Pessoa("Thiago", 30)
pessoa2 = Pessoa("Maria", 25)

print(pessoa1.apresentar())  # Olá, meu nome é Thiago e tenho 30 anos
print(pessoa2.apresentar())  # Olá, meu nome é Maria e tenho 25 anos
print(pessoa1.aniversario())  # Feliz aniversário Thiago! Agora tem 31 anos
