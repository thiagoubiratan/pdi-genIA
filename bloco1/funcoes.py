# função simples
def somar(a, b):
    return a + b

# função com valor padrão no parâmetro
def saudacao(nome, prefixo="Olá"):
    return f"{prefixo}, {nome}"

# chamando as funções
print(somar(5, 3))
print(saudacao("Thiago"))
print(saudacao("Thiago", "Bem-vindo"))