import json

CAMINHO_ARQUIVO = 'OrientacaoObjetos\classes.json'

class Pessoa:
    ano_atual = 2022
    
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Joao',35)
p2 = Pessoa('Helena', 12)
p3 = Pessoa('Josefa', 45)
bd = [vars(p1),vars(p2),vars(p3)]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('Fazendo dump!')
        json.dump(bd, arquivo,ensure_ascii=False, indent=2)

if __name__ == '__main__':
    fazer_dump()