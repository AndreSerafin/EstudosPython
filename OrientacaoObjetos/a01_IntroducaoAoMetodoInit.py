class Pessoa:
    def __init__(self, nome, sobrenome, idade) -> Pessoa:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def to_string(self):
        return f'Nome: {self.nome}, Sobrenome: {self.sobrenome}, Idade: {self.idade}'
        
p1 = Pessoa('Andre', 'Pereira', 22)
p2 = Pessoa('Maria', 'Joana', 28)

print(p1.to_string())
print(p2.to_string())