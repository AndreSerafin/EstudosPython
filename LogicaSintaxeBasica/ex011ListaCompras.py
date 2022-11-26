import os

op = ''

lista_de_compras = []

while op != 's':
    
    op = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar [s]air: ")
    
    if op == 'i':
        produto = input("Digite o nome do produto: ")
        lista_de_compras.append(produto)
    elif op == 'a':
        try:
            produto = input("Digite o indice a ser apagado: ")
            for i in range(len(lista_de_compras)):
                del lista_de_compras[int(produto)]
        
        except IndexError or ValueError:
            print("Indice inexistente")
            
    elif op == 'l':
        if len(lista_de_compras) == 0:
            print("Nada para listar!")
            input()
            os.system("clear")
            continue
        
        for i, nomes in enumerate(lista_de_compras):
            print(f"{i} {nomes}")
    elif op == 's':
        continue
    else:
        print("Opção inválida")
    input()
    os.system("clear")