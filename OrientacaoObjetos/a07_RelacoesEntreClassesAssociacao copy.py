class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None
        
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
        
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
        
    def escrever(self):
        return f'{self.nome} está escrevendo!'
    
escritor = Escritor('André')
escritor2 = Escritor('André2')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina = FerramentaDeEscrever('Maquina')

escritor.ferramenta = caneta
escritor2.ferramenta = maquina
print(escritor.ferramenta.escrever())
print(escritor2.ferramenta.escrever())