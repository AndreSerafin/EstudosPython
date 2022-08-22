import os

def add_parte(num_tentativas):
        os.system("cls" if(os.name == "nt" ) else "clear")
        if(num_tentativas == 0):
            print("   __")
            print("  |  \\")
            print("  |   |  ")
            print("  |")
            print("  |")
            print("  |")
            print(" _|_")
        elif(num_tentativas == 1):
            print("   __")
            print("  |  \\")
            print("  |   |  ")
            print("  |   O")
            print("  |")
            print("  |")
            print(" _|_")
        elif(num_tentativas == 2):
            print("   __")
            print("  |  \\")
            print("  |   |  ")
            print("  |   O")
            print("  |   |")
            print("  |")
            print(" _|_")
        elif(num_tentativas == 3):
            print("   __")
            print("  |  \\")
            print("  |   |  ")
            print("  |   O")
            print("  |  /|")
            print("  |")
            print(" _|_")
        elif(num_tentativas == 4):
            print("   __")
            print("  |  \\")
            print("  |   |  ")
            print("  |   O")
            print("  |  /|\\")
            print("  |")
            print(" _|_")
        elif(num_tentativas == 5):
            print("   __")
            print("  |  \\")
            print("  |   |  ")
            print("  |   O")
            print("  |  /|\\")
            print("  |  /")
            print(" _|_")
        elif(num_tentativas == 6):
            print("   __")
            print("  |  \\")
            print("  |   |  ")
            print("  |   O")
            print("  |  /|\\")
            print("  |  / \\")
            print(" _|_")
        elif(num_tentativas > 6):
            print("   __")
            print("  |  \\")
            print("  |   |  ")
            print("  |   0")
            print("  |  /|\\")
            print("  |  / \\")
            print(" _|_")

def testa_palpite(palpite, palavra_secreta):
    
    palavra_secreta = str(palavra_secreta)
    palpite = str(palpite)
    letra = []

    letra_presente = False
    for i in list(palavra_secreta):
        if(i == palpite):
            letra.append(palpite)
            letra_presente = True
        else:
            letra.append("_")
    return letra , letra_presente
            


def jogar_forca():
    print("--------------------------")
    print("Bem vindo ao jogo da Forca!")
    print("--------------------------")

    palavra_secreta = "banana"
    total_tentativas = 6
    num_tentativa = 0

    print("PALAVRA: " + "_ " * len(palavra_secreta))
    forma_palavra_lista = list("_" * len(palavra_secreta))

    while(num_tentativa <=6 or chute != palavra_secreta):
        add_parte(num_tentativa)



        palavra = " ".join(map(str,forma_palavra_lista))
        if("".join(map(str,forma_palavra_lista)) == palavra_secreta):
            print("Parabéns você Venceu!")
            break
        print("\nPALAVRA: ",palavra,"\n")
        op = int(input("1) chutar letra: 2) chutar palavra: "))


        if(op == 1):
            chute_letra = input("Digite uma letra: ").lower().strip()
            
            if (testa_palpite(chute_letra, palavra_secreta)[1] == True):
                palavra_lista = testa_palpite(chute_letra, palavra_secreta)[0]
                for i in range(len(palavra_lista)):
                    if(palavra_lista[i] != "_"):
                        forma_palavra_lista[i] = palavra_lista[i]
            else:
                print("A letra não está presente!")
                num_tentativa += 1
                add_parte(1)
            

        elif(op == 2):
            chute = input("Digite uma palavra: ").lower().strip()
            if(chute != palavra_secreta):
                num_tentativa = 6
                add_parte(num_tentativa)
                print("\nPALAVRA: ",palavra_secreta,"\n")
                print("Palavra errada!\n")
                break
            else:
                palavra_secreta = chute
                add_parte(num_tentativa)
                print("Parabéns Palavra correta!")
                break
        input()

    print("Fim do Jogo")

if(__name__ == "__main__"):

    jogar_forca()

