import math

documentos = ["use a cabeca java.pdf", "C# stap by stap.pdf", "java em 21 dias.pdf", "C# com TDD.pdf"]
paginas = [5, 48, 55, 68]
idiomas = ["pt", "en", "es", "pt"]

qtde_documentos_longos = 0
documentos_longos = []
documentos_medios = []
documentos_longos_pt = []

tentativa = 0

def classificar(paginas):
    if paginas > 50:
        return "longo"
    if paginas > 10:
        return "medio"
    return "curto"

def estimar_minutos(paginas, por_minuto=3):
    paginas_por_minuto = paginas / por_minuto
    return math.ceil(paginas_por_minuto)

print("====== Catalogo ======")

for i, documento in enumerate(documentos):
    tipo = classificar(paginas[i])
    minutos_por_leitura = estimar_minutos(paginas[i])
    
    if tipo == "longo":
        qtde_documentos_longos += 1
        documentos_longos.append(i)

    if paginas[i] > 10:
        documentos_medios.append(documento)

    if paginas[i] > 50 and idiomas[i] == "pt":
        documentos_longos_pt.append(documento)

    print(i+1, "|", "Nome:", documento, "|", "paginas:", paginas[i], "|", "idioma:", idiomas[i], "|", "minutos por leitura:", minutos_por_leitura)

print("Documentos longos:", qtde_documentos_longos)

print("===== Para Indexar =======")
print("Documentos com mais de 10 páginas:", documentos_medios)

print("===== Longos em Portuges =====")
print("Documentos longos em Portuges:", documentos_longos_pt)

while tentativa < 3:
    tentativa += 1
    print("Tentativa de numero", tentativa, "de conexao")

for i in range(3):
    print("-" * 20)