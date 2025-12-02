class ProdutoController:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def listar(self):
        return self.produtos

    def atualizar(self, id, novo_produto):
        for p in self.produtos:
            if p.get_id() == id:
                p.set_nome(novo_produto.get_nome())
                p.set_preco(novo_produto.get_preco())
                p.set_quantidade(novo_produto.get_quantidade())
                return True
        return False

    def remover(self, id):
        for p in self.produtos:
            if p.get_id() == id:
                self.produtos.remove(p)
                return True
        return False