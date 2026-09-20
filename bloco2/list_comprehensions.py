# jeito tradicional
numeros = []
for i in range(10):
    numeros.append(i)
print(numeros)

# com list comprehension
numeros = [i for i in range(10)]
print(numeros)

# com condição só pares
pares = [i for i in range(10) if i % 2 == 0]
print(pares)

# transformando os valores — dobrando cada número
dobrados = [i * 2 for i in range(10)]
print(dobrados)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]