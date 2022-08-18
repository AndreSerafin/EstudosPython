print("----------------------------------")
print("Bem vindo ao jogo de adivinhação!")
print("----------------------------------")

numero_secreto = 42
num_tentativas = 1
max_tentativas = 3

while (num_tentativas <= max_tentativas):
    chute = int(input("Digite o seu numero: "))
    
    print(f"Tentativa {num_tentativas} de {max_tentativas}")

    if (numero_secreto == chute):
        print("Você acertou!")
        break
    elif(chute > numero_secreto):
        print("Voce errou! O seu chute foi maior do que o numero secreto")
    elif(chute < numero_secreto):
        print("Voce errou! O seu chute foi menor do que o numero secreto")
    
    num_tentativas += 1

print("Fim do jogo")