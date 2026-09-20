usuario = "Thiago"
senha = "1234"
idade = 2

if usuario == "Thiago" and senha == "1234":
    if idade >= 18:
        print("Acesso liberado")
    else:
        print("Acesso negado - menor de idade")
else:
    print("Usuário ou senha incorretos")
