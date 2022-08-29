from operator import add
import os
from random import randint


def add_parte(num_tentativas, palavra, chutes_anteriores):
        os.system("cls" if(os.name == "nt" ) else "clear")
        str1_formatada = "   ".join(map(str, palavra[0:]))
        str2_formatada = "   ".join(map(str, chutes_anteriores[0:]))
        print("   __")
        print("  |  \\")
        print("  |   |  " + str2_formatada)
        if(num_tentativas == 0):
            print("  |")
            print("  |")
            print("  |")
            print("  |")
        elif(num_tentativas == 1):
            print("  |   O")
            print("  |")
            print("  |")
            print("  |")
        elif(num_tentativas == 2):
            print("  |   O")
            print("  |   |")
            print("  |")
            print("  |")
        elif(num_tentativas == 3):
            print("  |   O")
            print("  |  /|")
            print("  |")
            print("  |")
        elif(num_tentativas == 4):
            print("  |   O")
            print("  |  /|\\")
            print("  |")
            print("  |")
        elif(num_tentativas == 5):
            print("  |   O")
            print("  |  /|\\")
            print("  |  /")
            print("  |")
        elif(num_tentativas == 6):
            print("  |   O")
            print("  |  /|\\")
            print("  |  / \\")
            print("  |")
        elif(num_tentativas > 6):
            print("  |   O")
            print("  |")
            print("  |  /|\\")
            print("  |  / \\")
        print(" _|_      ", str1_formatada)


def verifica_letra(palavra_secreta, letra):
    
    forma_palavra = []
    esta_presente = False

    for i in palavra_secreta:
        if (i == letra):
            forma_palavra.append(letra)
            esta_presente = True
        else:
            forma_palavra.append("_")

    return forma_palavra, esta_presente
            

def junta_letras(aux1, junta_letras):
    
    
    for i in range(0,len(aux1)):
        
        if (aux1[i] != "_"):
            junta_letras[i] = aux1[i]
        
    return junta_letras

def define_palavra_secreta():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    nome_arquivo = dir_path + "/lista.txt"
    with open(nome_arquivo, "r") as file:
        
        linhas = file.read()
        palavras = list(map(str, linhas.split()))

        linha_aleatoria = randint(0,245365)
        palavra_secreta = palavras[linha_aleatoria]
        return palavra_secreta

def jogar_forca():
    
    palavra_secreta = define_palavra_secreta().upper()
    tam_palavra_sec = len(palavra_secreta)

    enforcou = False
    max_tentativas = 6

    juntando_letras = ["_"] * tam_palavra_sec
    numero_tentativas = 0
    chutes_anteriores = []
    add_parte(numero_tentativas, juntando_letras, chutes_anteriores)

    while(enforcou == False and numero_tentativas <= max_tentativas):

        chute = input("Digite uma letra ou a palavra completa: ").upper()
        tam_chute = len(chute)

        if (tam_chute == 1):
            if (verifica_letra(palavra_secreta, chute)[1]):
                aux1 = verifica_letra(palavra_secreta, chute)[0]
                juntando_letras = junta_letras(aux1,juntando_letras)
                add_parte(numero_tentativas, juntando_letras,chutes_anteriores)
                if(juntando_letras[0:] == list(palavra_secreta)[0:]):
                    print("Parabéns Você Descobriu a Palavra Secreta!")
                    break
            else:
                numero_tentativas += 1
                chutes_anteriores.append(chute)
                add_parte(numero_tentativas, juntando_letras, chutes_anteriores)

                print(f"A letra {chute} não está presente!")
                if(numero_tentativas > max_tentativas):
                    print(f"Você não descobriu a palavra! \n\n A Palavra era: {palavra_secreta}\n\nFIM DE JOGO!")
                input("\nPressione enter para continuar ")
        elif (tam_chute > 1):
            if (palavra_secreta == chute):
                add_parte(numero_tentativas, palavra_secreta)
                print("\nParabéns Você Acertou!")
                numero_tentativas = 6
            else:
                enforcou = True
                print(f"\nVocê errou! \n\n A Palavra era: {palavra_secreta}\n\nFIM DE JOGO!")




if (__name__ == "__main__"):
    jogar_forca()