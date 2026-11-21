paginas = [5, 48, 55, 68]
nomes = ["setup.pdf", "lgpd.pdf", "paper.pdf"]

#cria a lambda
metade = lambda x: x / 2

# chama ela como qualquer função
print(metade(100))
print(metade(paginas[3]))

print(sorted(nomes))
print(sorted(nomes, key=lambda n: len(n)))