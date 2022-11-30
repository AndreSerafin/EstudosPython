class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome}, já está filmando')
            return
        print(f'{self.nome} está filmando...!')
        self.filmando = True
    
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome}não está filmando')
            return
        print(f'{self.nome} está parando de filmar...!')
        self.filmando = False
        
    def foto(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquando filma')
            return
        
        print(f'{self.nome} esta fotografando')
        self.foto = True
        
c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.foto()
c1.parar_filmar()
c1.foto()
print()
c2.filmar()
c2.filmar()
c2.foto()
c2.foto()
