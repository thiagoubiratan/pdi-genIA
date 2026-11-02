titulo = "Lei Geral de Protecao de dados"
paginas = 65
tamanho_mb = 1.78
indexado = False
idioma = "pt"

lista_nome = ["Jose", "Antonio", "Carlos"]

print("Titulo:", titulo)
print("Tipo do titulo:", type(titulo))

print("Numero de paginas:", paginas)
print("Tipo de paginas:", type(paginas))

print("Tamanho:", tamanho_mb)
print("Tipo de tamanho_mb:", type(tamanho_mb))

print("Indexando:", indexado)
print("Tipo de indexacao", type(indexado))

print("Idioma:", idioma)
print("Tipo de idioma:", type(idioma))

print(lista_nome)
print(lista_nome[0])
print(len(lista_nome))

paginas_texto = str(paginas)
tamanho_int = int(tamanho_mb)

print("Paginas convertido:", paginas_texto, type(paginas_texto))
print("Tamanho convertido:", tamanho_int, type(tamanho_int))