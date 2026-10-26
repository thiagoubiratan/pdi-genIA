import re

from pypdf import PdfReader


def decodificar(texto):
    # Troca cada /uniXXXX pela letra correspondente
    return re.sub(r"/uni([0-9A-Fa-f]{4})", lambda m: chr(int(m.group(1), 16)), texto)

leitor = PdfReader("docs/http___www.planalto.gov.br_ccivil_03__ato2015-2018_2018_lei_L13.pdf")

print(f"Total de páginas: {len(leitor.pages)}\n")

texto_completo = ""
for pagina in leitor.pages:
    texto_completo += decodificar(pagina.extract_text()) + "\n"

print(f"Total de caracteres: {len(texto_completo)}\n")

print("--- INÍCIO DO TEXTO ---")
print(texto_completo[:1000])
print("--- FIM DA AMOSTRA ---")