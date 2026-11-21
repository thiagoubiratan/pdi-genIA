from pydantic import BaseModel, ValidationError


class Documento(BaseModel):
    nome: str
    paginas: int
    idioma: str
    indexado: bool


d = Documento(nome="paper.pdf", paginas=10, idioma="pt-br", indexado=False)

print(d)
print(d.nome)

d2 = Documento(nome="paper.pdf", paginas="120", idioma="pt-br", indexado=False)
print(type(d2.paginas))

# "muitas" nao da para converter em int: o Pydantic recusa e levanta ValidationError
try:
    d3 = Documento(nome="erro.pdf", paginas="muitas", idioma="pt-br", indexado=False)
    print(d3)
except ValidationError as e:
    print("documento invalido:")
    print(e)