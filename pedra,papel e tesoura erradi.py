import random

def jogar():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    jogador_escolha = int(input("Digite o número correspondente à sua escolha: "))

    if jogador_escolha < 1 or jogador_escolha > 3:
        print("Escolha inválida. Tente novamente.")
        jogar()
    else:
        if jogador_escolha == 1:
            jogador_escolha_nome = "Pedra"
        elif jogador_escolha == 2:
            jogador_escolha_nome = "Papel"
        else:
            jogador_escolha_nome = "Tesoura"

        print("Você escolheu: " + jogador_escolha_nome)

        escolhas = ["Pedra", "Papel", "Tesoura"]
        computador_escolha = random.choice(escolhas)
        print("O computador escolheu: " + computador_escolha)

        if jogador_escolha_nome == computador_escolha:
            print("Empate!")
        elif (
            (jogador_escolha_nome == "Pedra" and computador_escolha == "Tesoura") or
            (jogador_escolha_nome == "Papel" and computador_escolha == "Pedra") or
            (jogador_escolha_nome == "Tesoura" and computador_escolha == "Papel")
        ):
            print("Você venceu!")
        else:
            print("Você perdeu!")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() == "s":
            jogar()
        else:
            print("Obrigado por jogar!")

jogar()