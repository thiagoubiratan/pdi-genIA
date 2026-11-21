with open ("Notas.txt", "w", encoding="UTF-8") as arquivo:
    arquivo.write("lgpd.pdf\n")
    arquivo.write("paper.pdf\n")
    arquivo.write("setup.pdf\n")

with open ("Notas.txt", "r", encoding="UTF-8") as arquivo:
    conteudo_de_notas = arquivo.read()

print(conteudo_de_notas)