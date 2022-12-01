class Carrinho:
    def __init__(self, ):
        self._produtos = []
    
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def insere_produtos(self, *produtos):
        for i in produtos:
            self._produtos.append(i)
        
    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome_produto, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome_produto = nome
        self.preco = preco
    

carrinho = Carrinho()

p1, p2 = (Produto('Alface', 9.0), Produto('Arroz', 9.5))

carrinho.insere_produtos(p1,p2)
carrinho.listar_produtos()