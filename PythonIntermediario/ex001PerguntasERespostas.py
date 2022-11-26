from random import randint
import os
from ast import literal_eval

arquivo = open('PythonIntermediario/perguntas.txt', 'r', encoding='UTF-8')

perguntas = literal_eval(arquivo.read())

pontuacao = 0
perguntas_sortedas = set()

for i in range(len(perguntas)):
    
    randomizador_de_perguntas = randint(0, len(perguntas) - 1)
    
    while randomizador_de_perguntas in perguntas_sortedas:
        randomizador_de_perguntas = randint(0, len(perguntas) - 1)
    perguntas_sortedas.add(randomizador_de_perguntas)
    
    pergunta = perguntas[randomizador_de_perguntas]
    
    print(pergunta['Pergunta'])
    
    opcoes = pergunta['Opcoes'][0]
    
    for opcao in opcoes.keys():
      print(f'{opcao}) {opcoes[opcao]}') 
      
    resposta = input('Digite sua resposta: ')
    
    resposta_certa = pergunta['Resposta'][0]
    if resposta in resposta_certa.keys() or resposta in resposta_certa.values():
        pontuacao += 1
        print('Correto! ✔', f'Pontuação: {pontuacao}')
    else:
        print('Incorreto! ❌', f'Pontuação: {pontuacao}')
    print('\n')
    input('Aperter enter para proxima pergunta   ')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
print(f'👏👏Você acertou {pontuacao} de {len(perguntas)} peguntas👏👏')
        