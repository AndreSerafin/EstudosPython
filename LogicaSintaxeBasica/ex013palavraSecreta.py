import os

palavra_secreta = "Perfume".lower()
letras_acertadas = ""
acertou = False
tentativas = 0

while not acertou:
    
    chute = input("Digite uma letra: ")
    
    if len(chute) > 1:
        print("Digite apenas uma letra")
        continue
    
    if chute in palavra_secreta:
        letras_acertadas += chute
    
    palavra_final = ""
    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_final += i
        else:
            palavra_final += "*"
            
    tentativas += 1
    print(palavra_final)
    if palavra_final == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        acertou = True
        print(f"Parabéns vc acertou a palavra secreta, com {tentativas} tentativas")