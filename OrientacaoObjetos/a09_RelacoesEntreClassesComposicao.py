class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
        
    def iserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for i in self.enderecos:
            print(f'Rua: {i.rua}, Numero: {i.numero}')
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
        
c1 = Cliente('Maria')
c1.iserir_endereco('PP14', 31)
c1.iserir_endereco('PP13', 33)
c1.iserir_endereco('Av. Brasil', 1133)

c1.listar_enderecos()