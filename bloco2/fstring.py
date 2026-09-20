nome = "Thiago"
idade = 30
altura = 1.75

# f-string básica
print(f"Meu nome é {nome}")  # Meu nome é Thiago

# com expressões dentro
print(f"Daqui a 10 anos terei {idade + 10} anos")  # Daqui a 10 anos terei 40 anos

# formatando números
print(f"Altura: {altura:.1f}")   # Altura: 1.8 — 1 casa decimal
print(f"Altura: {altura:.2f}")   # Altura: 1.75 — 2 casas decimais

# formatando inteiros com zeros à esquerda
numero = 5
print(f"Número: {numero:03d}")   # Número: 005

# maiúsculas e minúsculas
print(f"{nome.upper()}")   # THIAGO
print(f"{nome.lower()}")   # thiago