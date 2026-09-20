# com tratamento
try:
    numero = int("ABC")
    print(numero)
except ValueError:
    print("Valor Inválido - não é um número")

# capturado erros diferentes
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Divisão por zerp não permitida")
except ValueError:
    print("valor invalido")

# finally - executa sempre, com ou sem erro
try:
    numero = int("123")
    print(f"número {numero}")
except ZeroDivisionError:
    print("Divisão por zero não permitida")
finally:
    print("Isso sempre executa")