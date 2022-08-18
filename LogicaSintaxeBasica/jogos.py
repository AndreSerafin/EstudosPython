from ex004Forca import jogar_forca
from ex003AdivinhacaoFor import jogar_adivinhacao

def escolha_jogo():
    print("--------------------------")
    print("----Escolha seu jogo!-----")
    print("--------------------------")

    print("(1) Forca (2) Adivinhação")

    jogo = int (input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        jogar_forca()
    elif(jogo == 2):
        print("Jogando adivinhação")
        jogar_adivinhacao()

if(__name__ == "__main__"):
    escolha_jogo()