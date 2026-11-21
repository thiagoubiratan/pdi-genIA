import math


class Documento:
    # construtor: roda quando voce faz Documento("lgpd.pdf", 65, "pt")
    def __init__(self, nome, paginas, idioma):
        self.nome = nome
        self.paginas = paginas
        self.idioma = idioma

    # metodo: recuado 4 espacos, dentro da classe.
    # so recebe self, porque usa os dados que o proprio objeto ja tem.
    def estimar_minutos(self):
        return math.ceil(self.paginas / 3)

    def resumo(self):
        return f"{self.nome} | {self.paginas} pag | {self.idioma}"


# fora da classe: margem zero, sem recuo
doc1 = Documento("lgpd.pdf", 65, "pt")
doc2 = Documento("setup.pdf", 8, "en")

print(doc1.resumo())
print("minutos de leitura:", doc1.estimar_minutos())

print(doc2.resumo())
print("minutos de leitura:", doc2.estimar_minutos())