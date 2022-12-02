from xml.etree import ElementTree as ET
import requests
from datetime import date

def cria_url(ano,dtInicio,dtFim):
    url = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes?ano={}&dataApresentacaoInicio={}&dataApresentacaoFim={}&ordem=ASC&ordenarPor=id'
    return url.format(ano, dtInicio, dtFim)

def abre_url(url):
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()
    else:
        return None
    
def percorre(dicionario):
    dados = dicionario['dados']
    for i in range(len(dicionario['dados'])):
        print(f"\nid : {dados[i]['id']}, ano: {dados[i]['ano']}")
        print(f"ementa : {dados[i]['ementa']}\n")
        
def dados_digitados():
    ano = int(input('Digite o ano que deseja buscar: '))
    if ano < 1989 or ano > date.today().year:
        raise ValueError
    dataIncio = input('Data de inicio(dd/mm): ')
    dataFim = input('Data de Finalização: ')
    
    dataIncioForm = str(ano) + '-' + dataIncio[3:5] + '-' + dataIncio[0:2]
    dataFimForm = str(ano) + '-' + dataFim[3:5] + '-' + dataFim[0:2]
    return ano,dataIncioForm, dataFimForm
    
    
if __name__ == '__main__':
    print('-------Buscador de PLs-------')
    
    flag = False
    dados_busca = None
    
    while not flag:
        try:
            dados_busca = dados_digitados()
            flag = True
        except ValueError:
            print('Valor inválido!')
        
    
    
    dados = abre_url(cria_url(dados_busca[0],dados_busca[1], dados_busca[2]))
    percorre(dados)