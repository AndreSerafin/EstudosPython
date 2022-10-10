from random import randint
print("*******-Gerador de CPF-*******\n")
op = 's'

while op != 'n':
    cpf = ""
    for i in range(9):
        cpf += str(randint(0,9))

    lista_multipicados = []

    for i,j in zip(cpf, range(10,1,-1)):
        lista_multipicados.append(int(i)*j)

    soma = sum(lista_multipicados)

    dig1 = 11 - (soma % 11)
    if dig1 > 9:
        dig1 = 0

    cpf += str(dig1)

    lista_multipicados = []
    for i,j in zip(cpf, range(11,1,-1)):
        lista_multipicados.append(int(i)*j)

    soma = sum(lista_multipicados)
    dig2 = 11 - (soma % 11)
    if dig2 > 9:
        dig2 = 0

    cpf += str(dig2)
    print(f"Cpf gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    op = input("Deseja gerar outro cpf(s/n)? ")
