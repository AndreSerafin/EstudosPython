class Pessoa:
    ano = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('Anonima', idade)
    
p1 = Pessoa('Joao', 34)
p2 = Pessoa.criar_com_50_anos('Joana')

p3 = Pessoa.criar_sem_nome(30)

print(p1.__dict__)
print(p2.__dict__)
print(p3.__dict__)

p2.__setattr__('sobrenome', 'pereira')
print(p2.__dict__)
print(p2.__getattribute__('nome'))