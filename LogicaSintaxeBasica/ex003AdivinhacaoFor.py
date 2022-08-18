import random


def jogar_adivinhacao():
    print("----------------------------------")
    print("Bem vindo ao jogo de adivinhação!")
    print("----------------------------------")

    numero_secreto = random.randint(1,101)

    print("Qual nivel de dificuldade: ")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Selecione o nivel: "))

    match nivel:
        case 1:
            max_tentativas = 15
        case 2:
            max_tentativas = 9
        case 3:
            max_tentativas = 5

    pontuacao_max = 1000

    for rodada in range(1,max_tentativas + 1):
        chute = int(input("Digite um número entre 1 e 100: "))
        if (chute >= 1 and chute <= 100):
            print(f"Tentativa {rodada} de {max_tentativas}")

            if (numero_secreto == chute):
                print("Você acertou!")
                print(f"Pontos: {pontuacao_max}")
                break
            elif(chute > numero_secreto):
                print("Voce errou! O seu chute foi maior do que o numero secreto")
                pontuacao_max -= chute - numero_secreto
            elif(chute < numero_secreto):
                print("Voce errou! O seu chute foi menor do que o numero secreto")
                pontuacao_max -= numero_secreto - chute
        else:
            print("Chute fora do intervalo esperado")
            continue

        if (rodada == max_tentativas): 
            pontuacao_max = 0
            print("\nPontos:",pontuacao_max)

        

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_adivinhacao()
