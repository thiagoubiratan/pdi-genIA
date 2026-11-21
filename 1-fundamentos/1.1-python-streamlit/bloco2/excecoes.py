valores = ["10", "abc", "25", "3.5"]

for x in valores:
    try:
        numero = int(x)
        print(numero)
    except ValueError as e:
        print("mensagem de erro:", e)

