from random import randint

op = ''

while op != 'n':
    cpf = str(randint(100000000,999999999))

    soma = 0

    for i, j in enumerate(range(10,1,-1)):
        soma += j * int(cpf[i])
        
    multiplicado = soma * 10

    resto_div = multiplicado % 11

    prim_dig = 0 if resto_div > 9 else resto_div

    cpf += str(prim_dig)

    soma = 0
    for i, j in enumerate(range(11,1,-1)):
        soma += j * int(cpf[i])
        
    multiplicado = soma * 10

    resto_div = multiplicado % 11

    seg_dig = 0 if resto_div > 9 else resto_div

    cpf += str(seg_dig)

    print(f"Cpf gerado: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    op = input("Deseja gerar outro cpf [s]im [n]ão: ")

