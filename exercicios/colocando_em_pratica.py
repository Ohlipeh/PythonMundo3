from random import choice

jogador = 0

campeoes = (
    "Aatrox",
    "Ahri",
    "Akali",
    "Alistar",
    "Amumu",
    "Anivia",
    "Annie",
    "Aphelios",
    "Ashe",
    "Aurelion Sol",
    "Azir",
    "Bard",
)

print("-" * 30)
print("\033[1;33;44m---------- X1 - LOL ----------\033[m")
print("-" * 30)

while True:

    print("\033[1;31m1 - Selecionar pro X1\033[m")
    print("\033[1;35m2 - Selecionar uma frase do campeão\033[m")
    print("\033[1;33m3 - Sair do programa\033[m")

    print("-" * 30)

    opcao = int(input("\033[1mDigite a opção desejada: \033[m"))

    if opcao == 1:
        print("\nCampeões disponíveis:")
        for campeao in campeoes:
            print(campeao)

        jogador = input("\nDigite o nome do campeão para o X1: ").strip().capitalize()

        if jogador in campeoes:
            adversario = choice(campeoes)

            print("-" * 30)
            print("\033[1;32mBATTLE START!\033[m")
            print(f"\033[1;32m{jogador} X {adversario}\033[m")
            print("-" * 30)

            vencedor = choice([jogador, adversario])
            print(f"\033[1;34mO vencedor é: {vencedor}!\033[m")
            print("-" * 30)

        else:
            print("Campeão não encontrado. Tente novamente.")

    elif opcao == 2:
        print("\nCampeões disponíveis:")
        print("-" * 30)

        for campeao in campeoes:
            print(campeao)
        frases = {
            "Aatrox": "Eu sou a espada de Shurima!",
            "Ahri": "Não se preocupe, eu só quero brincar!",
            "Akali": "O silêncio é a minha arma mais poderosa.",
            "Alistar": "Eu sou o Minotauro, e ninguém me detém!",
            "Amumu": "Por que todos me abandonam?",
            "Anivia": "O inverno está chegando.",
            "Annie": "Vamos brincar de fogo!",
            "Aphelios": "A escuridão é minha aliada.",
            "Ashe": "O gelo é minha arma.",
            "Aurelion Sol": "Eu criei as estrelas, e agora vou destruí-las!",
            "Azir": "O império de Shurima ressurgirá!",
            "Bard": "O universo é cheio de mistérios, e eu estou aqui para explorá-los!",
        }
        campeao = (
            input("\nDigite o nome do campeão para ouvir uma frase: ")
            .strip()
            .capitalize()
        )
        print("-" * 40)

        if campeao in frases:
            print(f"\033[1;36m{campeao} diz: '{frases[campeao]}'\033[m")
        else:
            print("Campeão não encontrado. Tente novamente.")
        print("-" * 40)

    elif opcao == 3:
        print("Saindo do programa. Até a próxima!")
        break
