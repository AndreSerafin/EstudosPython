class Pessoa:
    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome
        
    def falar_nome_classe(self):
        print(f'{self._nome}, {self._sobrenome} - {self.__class__.__name__}')
    
class Cliente(Pessoa):
    ...
    
class Aluno(Pessoa):
    ...

c1 = Cliente('Andre', 'Pereira')
c1.falar_nome_classe()

a1 = Aluno('Joao', 'Santos')
a1.falar_nome_classe()
