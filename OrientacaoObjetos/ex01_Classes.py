# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None
           
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante
        
    def vizualiza_carro(self):
        print(f'Nome: {self._nome}, Motor: {self._motor.nome}, Fabricante: {self._fabricante.nome}')
        
class Motor:
    def __init__(self, nome):
        self._nome = nome
    @property
    def nome(self):
        return self._nome

class Fabricante:
    def __init__(self, nome):
        self._nome = nome
    @property
    def nome(self):
        return self._nome
        
m1 = Motor('1.0')
f1 = Fabricante('Wolkswagen')
c1 = Carro('Fusca')

c1.fabricante = f1
c1.motor = m1
c1.vizualiza_carro()

c2 = Carro('Gol')
c2.fabricante = f1
c2.motor = m1
c2.vizualiza_carro()

m2 = Motor('1.5')
f2 = Fabricante('Fiat')
c3 = Carro('Palio')

c3.fabricante = f2
c3.motor = m2
c3.vizualiza_carro()
