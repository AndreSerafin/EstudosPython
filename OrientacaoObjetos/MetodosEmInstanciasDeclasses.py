class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca
        
    def acelerar(self):
        print('acelerando!')
        
fusca = Carro('Fusca', 'Volks')
celta = Carro('Celta', 'Volks')

print(fusca.nome)
fusca.acelerar()
print(fusca.marca)