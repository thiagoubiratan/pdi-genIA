import asyncio


async def processar(nome, segundos):
    await asyncio.sleep(segundos)
    print(f"{nome} terminou")


async def main():
    await asyncio.gather(
        processar("doc3", 3),
        processar("doc2", 2),
        processar("doc1", 1)
    )


asyncio.run(main())
