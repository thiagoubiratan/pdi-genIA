import random

vida_personagem = 100
monstros = [
    {"nome": "Goblin", "vida": 100},
    {"nome": "Orc", "vida": 100},
    {"nome": "Dragão", "vida": 100},
]


# e uma função para exibir o status do combate
def atacar(mostro, personagem):
    print(f"mostro : {mostro} X personagem: {personagem}")
    if mostro <= 0:
        print("fim do jogo, personagem ganhou")
    elif personagem <= 0:
        print("fim do jogo, mostro ganhou")
    else:
        print("continua luta")


# seu código aqui — use for para percorrer os monstros,
for monstro in monstros:
    print(f"Montro: {monstro['nome']} iniciando ataque, sua vida é {monstro['vida']}")

    # while para o combate durar até um dos dois morrer
    while monstro['vida'] != 0 and vida_personagem != 0:

        # random.randint(min, max) para gerar dano aleatório,
        ataque_mostro = random.randint(1, 9)
        ataque_personagem = random.randint(1, 9)

        vida_personagem -= ataque_mostro
        monstro['vida'] -= ataque_personagem

        atacar(vida_personagem, monstro['vida'])

        if vida_personagem <= 0 or monstro['vida'] <= 0:
            print(f"Fim de jogo para {monstro['nome']}!")
            vida_personagem = 100
            break
