paginas = [5, 48, 55, 68]
nomes = ["lgpd.pdf", "paper.pdf", "setup.pdf"]

triplo = [p * 3 for p in paginas]
print(triplo)

nome = [n.upper() for n in nomes]
print(nome)

paginas_menores_cinquenta = [p for p in paginas if p < 50]
print(f"Páginas menores que cinquenta {paginas_menores_cinquenta}")

dobro_paginas = [p * 2 for p in paginas if p > 40]
print(f"dobro de páginas maior que quarenta {dobro_paginas}")

nome_contem_p = [n for n in nomes if "a" in n]
print(nome_contem_p)