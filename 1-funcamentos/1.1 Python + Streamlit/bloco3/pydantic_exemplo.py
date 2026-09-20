from pydantic import BaseModel, ValidationError


# definindo um modelo com tipos
class Pessoa(BaseModel):
    nome: str
    idade: int
    email: str


# criando um objeto válido
pessoa = Pessoa(nome="Thiago", idade=30, email="thiago@email.com")
print(pessoa)
print(pessoa.nome)

# tentando criar com dados inválidos
try:
    pessoa_invalida = Pessoa(nome="Maria", idade="abc", email="maria@email.com")
except ValidationError as e:
    print(f"Erro de validação: {e}")
