print("*******-Verificador de CPF-*******\n")
op = 's'

while op != 'n':
    chars = ".-"
    cpf = input("Digite um cpf: ").translate(str.maketrans('','',chars))
    cpf_aux = cpf[:9]
    lista_multipicados = []

    for i,j in zip(cpf_aux, range(10,1,-1)):
        lista_multipicados.append(int(i)*j)

    soma = sum(lista_multipicados)

    dig1 = 11 - (soma % 11)
    if dig1 > 9:
        dig1 = 0

    cpf_aux += str(dig1)

    lista_multipicados = []
    for i,j in zip(cpf_aux, range(11,1,-1)):
        lista_multipicados.append(int(i)*j)

    soma = sum(lista_multipicados)
    dig2 = 11 - (soma % 11)
    if dig2 > 9:
        dig2 = 0

    cpf_aux += str(dig2)

    sequencia = cpf_aux == str(cpf_aux[0]) * 11

    if cpf_aux == cpf and not sequencia:
        print("O cpf é valido!")
    else:
        print("O cpf não é valido!")
    op = input("Deseja gerar outro cpf(s/n)? ")
