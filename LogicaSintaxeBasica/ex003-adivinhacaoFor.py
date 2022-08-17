import random
print("----------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("----------------------------------")

numero_secreto = random.randint(1,100)
max_tentativas = 15

for rodada in range(1,max_tentativas + 1):
    chute = int(input("Digite um número entre 1 e 100: "))
    
    if (chute >= 1 and chute <= 100):
        print(f"Tentativa {rodada} de {max_tentativas}")

        if (numero_secreto == chute):
            print("Você acertou!")
            break
        elif(chute > numero_secreto):
            print("Voce errou! O seu chute foi maior do que o numero secreto")
        elif(chute < numero_secreto):
            print("Voce errou! O seu chute foi menor do que o numero secreto")
    else:
        print("Chute fora do intervalo esperado")
        continue

print("Fim do jogo")