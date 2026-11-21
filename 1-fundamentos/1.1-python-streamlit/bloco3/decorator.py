def dizer_oi():
    print("Oi!")

f = dizer_oi

f()

def executar_tres_vezes(funcao):
    funcao()
    funcao()
    funcao()

executar_tres_vezes(dizer_oi)

def com_separador(funcao):
    def interna():
        print("-" * 20)
        funcao()
        print("-" * 20)
    return interna

@com_separador
def mostrar_titulo():
    print("Catalogo de PDFs")

mostrar_titulo()