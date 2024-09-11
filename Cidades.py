from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from apliCidade import Cidades

class Cidade:
    def __init__(self, master=None):
        self.master = master
        self.janela21 = Frame(master)
        self.janela21.pack()
        self.msg1 = Label(self.janela21, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela22 = Frame(master)
        self.janela22["padx"] = 20
        self.janela22.pack()

        self.idcidade_label = Label(self.janela22, text="Id cidade:")
        self.idcidade_label.pack(side="left")
        self.idcidade = Entry(self.janela22, width=20)
        self.idcidade.pack(side="left")

        self.busca = Button(self.janela22, text="Buscar", command=self.buscarCidade)
        self.busca.pack()

        self.janela23 = Frame(master)
        self.janela23["padx"] = 20
        self.janela23.pack()

        self.cidade_label = Label(self.janela23, text="Cidade:")
        self.cidade_label.pack(side="left")
        self.cidade = Entry(self.janela23, width=30)
        self.cidade.pack(side="left")

        self.janela24 = Frame(master)
        self.janela24["padx"] = 20
        self.janela24.pack(pady=5)

        self.uf_label = Label(self.janela24, text="UF:")
        self.uf_label.pack(side="left")
        self.uf = Entry(self.janela24, width=28)
        self.uf.pack(side="left")

        self.janela25 = Frame(master)
        self.janela25["padx"] = 20
        self.janela25.pack()

        self.autentic = Label(self.janela25, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        # Adicionando os botões para Inserir, Alterar e Excluir
        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack(pady=5)

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirCidade)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarCidade)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirCidade)
        self.botao3.pack(side="left")

        # Frame para a tabela
        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID","Cidade","UF"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.heading("UF", text="UF")
        self.tree.bind("<<TreeviewSelect>>", self.selecionacidade)
        self.tree.pack()

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

    def selecionacidade(self, event):

        seleciona_item = self.tree.selection()
        if seleciona_item:
            # Obtém o item selecionado
            item = seleciona_item[0]
            values = self.tree.item(item, 'values')
            # Preenche os campos de entrada com os dados do item selecionado
            self.idcidade.delete(0, END)
            self.idcidade.insert(INSERT, values[0])
            self.cidade.delete(0, END)
            self.cidade.insert(INSERT, values[1])
            self.uf.delete(0, END)
            self.uf.insert(INSERT, values[2])
    def atualizarTabela(self):
        cid = Cidades()
        cidades = cid.selectAllCidades()
        self.tree.delete(*self.tree.get_children())
        for c in cidades:
            self.tree.insert("acessado com sucesso", "fim", values=(c[0], c[1], c[2]))

    def buscarCidade(self):
        cid = Cidades()
        idcidade = self.idcidade.get()
        self.autentic["text"] = cid.selectCidade(idcidade)
        self.idcidade.delete(0, END)
        self.idcidade.insert(INSERT, cid.idcidade)
        self.cidade.delete(0, END)
        self.cidade.insert(INSERT, cid.cidade)
        self.uf.delete(0, END)
        self.uf.insert(INSERT, cid.uf)

    def inserirCidade(self):
        cid = Cidades(cidade=self.cidade.get(), uf=self.uf.get())
        result = cid.insertCidade()
        messagebox.showinfo("Sucesso",  result)
        #self.autentic["text"] = result
        self.atualizarTabela()
        self.master.focus_force()
        self.limpar_campos()

    def alterarCidade(self):
        cid = Cidades(idcidade=self.idcidade.get(), cidade=self.cidade.get(), uf=self.uf.get())
        result = cid.updateCidade()
        messagebox.showinfo("Sucesso", result)
        self.master.focus_force()
        #self.autentic["text"] = result
        self.atualizarTabela()
        self.limpar_campos()

    def excluirCidade(self):
        cid = Cidades(idcidade=self.idcidade.get())
        result = cid.deleteCidade()
        messagebox.showinfo("Sucesso", result)
        self.master.focus_force()
        #self.autentic["text"] = result
        self.atualizarTabela()
        self.limpar_campos()

    def limpar_campos(self):
        """Função para limpar o conteúdo dos campos Entry"""
        self.idcidade.delete(0, END)
        self.cidade.delete(0, END)
        self.uf.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    Cidade(root)
    root.mainloop()