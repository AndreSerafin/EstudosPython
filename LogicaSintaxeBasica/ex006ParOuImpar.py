# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

num_1 = input("Digite um número inteiro: ")
flag = False

while not flag:
    try:
        int_num_1 = int(num_1)
        if int_num_1 % 2 == 0:
            print(f"O número {num_1} é par")
        else:
            print(f"O número {num_1} é ímpar")
        flag = True
    except:
        print("Valor inválido")
        num_1 = input("Digite um número inteiro: ")