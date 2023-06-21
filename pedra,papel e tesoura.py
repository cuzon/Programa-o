import random # biblioteca que ja estava sendo usada

def jogar_pedra_papel_tesoura(jogada_jogador):
    jogadas = ["pedra", "papel", "tesoura"]
    jogada_Perdos = random.choice(jogadas)
# definições de qm é qm
    print(f"Você escolheu: {jogada_jogador}")
    print(f"O Perdos escolheu: {jogada_Perdos}") # nada melhor que me desafiar em um combate na base da pedrada

    if jogada_jogador == jogada_Perdos:# inves de usar números que poderá dar erros, irei usar da forma mais tradicional
        print("Empate!")
    elif (jogada_jogador == "pedra" and jogada_Perdos == "tesoura") or \
         (jogada_jogador == "papel" and jogada_Perdos == "pedra") or \
         (jogada_jogador == "tesoura" and jogada_Perdos == "papel"):
        print("Você venceu, verme!") # definições das jogadas de cada um
    else:
        print("O Perdos venceu!")

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ")
    return resposta.lower() == "s" # caso vc queira jogar novamente, como ja tinha antes

def jogo():
    print("Bem-vindo ao jogo, vamos jogar pedra na cabeça!") # na base da pedrada

    while True:
        jogada_jogador = input("Escolha sua jogada (pedra, papel ou tesoura, se não vc morrerá): ").lower() # mensagem para o jogador entender o que está acontecendo

        if jogada_jogador not in ["pedra", "papel", "tesoura"]:
            print("N faça isso de novo, se fizer te deixarei em pedaços, eventualmente")
            continue # usei o comando continue, depois do comando "if"

        jogar_pedra_papel_tesoura(jogada_jogador)

        if not jogar_novamente():
            break # "break" para dar um erro intencional para o jogador reiniciar o jogo

jogo()