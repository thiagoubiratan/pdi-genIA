for i in range(5):
    print(f"Número: {i}")

frutas = ["maçã", "Banana", "Uva"]
for i in frutas:
    print(f"Frutas: {i}")

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
