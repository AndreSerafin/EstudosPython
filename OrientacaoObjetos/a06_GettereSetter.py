# class Caneta:
#     def __init__(self, cor_tinta):
#         self.cor_tinta = cor_tinta
        
#     def get_cor(self):
#         return self.cor_tinta
        
        
# caneta1 = Caneta('Azul')
# print(caneta1.get_cor())


class Caneta:
    def __init__(self, cor_tinta):
        self._cor_tinta = cor_tinta
        
    @property
    def cor(self):
        return self._cor_tinta
    
    @cor.setter
    def cor(self, valor):
        self._cor_tinta = valor



    
caneta1 = Caneta('Azul')
print(caneta1.cor)
caneta1.cor = 'Verde'
print(caneta1.cor)