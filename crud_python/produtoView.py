import tkinter as tk
from tkinter import ttk, messagebox
from produto import Produto


class ProdutoView:
    def __init__(self, controller):
        self.controller = controller
        self.janela = tk.Tk()
        self.janela.title("Gerenciamento de Produtos")
        self.janela.geometry("600x400")

        
        tk.Label(self.janela, text="ID:").grid(row=0, column=0)
        tk.Label(self.janela, text="Nome:").grid(row=1, column=0)
        tk.Label(self.janela, text="Preço:").grid(row=2, column=0)
        tk.Label(self.janela, text="Quantidade:").grid(row=3, column=0)

        self.campo_id = tk.Entry(self.janela)
        self.campo_nome = tk.Entry(self.janela)
        self.campo_preco = tk.Entry(self.janela)
        self.campo_quantidade = tk.Entry(self.janela)

        self.campo_id.grid(row=0, column=1)
        self.campo_nome.grid(row=1, column=1)
        self.campo_preco.grid(row=2, column=1)
        self.campo_quantidade.grid(row=3, column=1)

        
        tk.Button(self.janela, text="Adicionar", command=self.adicionar).grid(row=4, column=0)
        tk.Button(self.janela, text="Listar", command=self.listar).grid(row=4, column=1)
        tk.Button(self.janela, text="Atualizar", command=self.atualizar).grid(row=4, column=2)
        tk.Button(self.janela, text="Remover", command=self.remover).grid(row=4, column=3)

        
        self.tabela = ttk.Treeview(self.janela, columns=("id", "nome", "preco", "quantidade"), show="headings")
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("preco", text="Preço")
        self.tabela.heading("quantidade", text="Qtd")
        self.tabela.grid(row=5, column=0, columnspan=4)

        self.janela.mainloop()

    # ------- FUNÇÕES DO CRUD ------- #

    def limpar(self):
        self.campo_id.delete(0, tk.END)
        self.campo_nome.delete(0, tk.END)
        self.campo_preco.delete(0, tk.END)
        self.campo_quantidade.delete(0, tk.END)

    def adicionar(self):
        try:
            id = int(self.campo_id.get())
            nome = self.campo_nome.get()
            preco = float(self.campo_preco.get())
            quantidade = int(self.campo_quantidade.get())

            p = Produto(id, nome, preco, quantidade)
            self.controller.adicionar(p)

            messagebox.showinfo("Sucesso", "Produto adicionado!")
            self.limpar()
            self.listar()
        except:
            messagebox.showerror("Erro", "Dados inválidos!")

    def listar(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for p in self.controller.listar():
            self.tabela.insert("", tk.END, values=(p.get_id(), p.get_nome(), p.get_preco(), p.get_quantidade()))

    def atualizar(self):
        try:
            id = int(self.campo_id.get())
            nome = self.campo_nome.get()
            preco = float(self.campo_preco.get())
            quantidade = int(self.campo_quantidade.get())

            novo = Produto(id, nome, preco, quantidade)

            if self.controller.atualizar(id, novo):
                messagebox.showinfo("Sucesso", "Produto atualizado!")
            else:
                messagebox.showerror("Erro", "Produto não encontrado!")

            self.limpar()
            self.listar()
        except:
            messagebox.showerror("Erro", "Dados inválidos!")

    def remover(self):
        try:
            id = int(self.campo_id.get())

            if self.controller.remover(id):
                messagebox.showinfo("Sucesso", "Produto removido!")
            else:
                messagebox.showerror("Erro", "Produto não encontrado!")

            self.limpar()
            self.listar()
        except:
            messagebox.showerror("Erro", "Dados inválidos!")