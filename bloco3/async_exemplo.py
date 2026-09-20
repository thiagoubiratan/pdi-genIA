import asyncio

# função assíncrona
async def buscar_dados(nome):
    print(f"Buscando dados de {nome}...")
    await asyncio.sleep(1)  # simula uma chamada a uma API
    return f"Dados de {nome} recebidos"

# executando uma função assíncrona
async def main():
    resultado = await buscar_dados("Thiago")
    print(resultado)

# ponto de entrada para código assíncrono
asyncio.run(main())