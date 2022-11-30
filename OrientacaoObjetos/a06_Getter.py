# class Caneta:
#     def __init__(self, cor_tinta):
#         self.cor_tinta = cor_tinta
        
#     def get_cor(self):
#         return self.cor_tinta
        
        
# caneta1 = Caneta('Azul')
# print(caneta1.get_cor())


class Caneta:
    def __init__(self, cor_tinta):
        self.cor_tinta = cor_tinta
        
    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456    
        
caneta1 = Caneta('Azul')
print(caneta1.cor)
print(caneta1.cor_tampa)