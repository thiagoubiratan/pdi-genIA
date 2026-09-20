# escrevendo arquivo
with open("teste.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# lendo arquivo
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# lendo linha por linha
with open("teste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove o \n do final

# adciona conteudo sem apagar o existente
with open("teste.txt", "a") as arquivo:
    arquivo.write("Terceira linha\n")

with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)