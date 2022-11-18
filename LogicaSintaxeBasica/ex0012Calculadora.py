opcao = ''
while opcao != 'S':
    num_1 = input("Digite o primeiro numero: ")
    operador = input("Digite o operador (=-/*): ")
    num_2 = input("Digite o segundo numero: ")

    float_num_1 = 0
    float_num_2 = 0
 
    try:
        float_num_1 = float(num_1)
        float_num_2 = float(num_2)
    except:
        print("Numeros inválidos")
        continue
            
    
    if len(operador) > 1:
        print("Digite apenas um operador!")
        continue
    
    resultado = 0
    
    if operador == '+':
        resultado = float_num_1 + float_num_2
    elif operador == '-':
        resultado = float_num_1 - float_num_2
    elif operador == '*':
        resultado = float_num_1 * float_num_2
    elif operador == '/':
        if float_num_2 > 0.0:
            resultado = float_num_1 / float_num_2
        else:
            print("Não é possível dividir um número por zero")
            continue
    else:
        print("Operador Iválido")
        continue
        
    print(f"{float_num_1} {operador} {float_num_2} = {resultado}")
    opcao = input("Deseja sair da calculadora [S]im [N]ão: ").upper()