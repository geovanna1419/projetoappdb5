from tkinter import *
from usuario import *

class Application:
    def __init__(self, master=None):
        self.janela1 = Frame(master)
        self.janela1.pack()
        self.msg1 = Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = Label(self.janela2, text="Id usuario:")
        self.idusuario_label.pack(side="left")
        self.idusuario = Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = Button(self.janela2)
        self.busca["text"] = "Buscar"
        self.busca["command"] = self.buscarUsuario
        self.busca.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.telefone_label = Label(self.janela5, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = Entry(self.janela5, width=28)
        self.telefone.pack(side="left")

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.email_label = Label(self.janela6, text="E-mail:")
        self.email_label.pack(side="left")
        self.email = Entry(self.janela6, width=30)
        self.email.pack(side="left")

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack(pady=5)

        self.usuario_label = Label(self.janela7, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = Entry(self.janela7, width=29)
        self.usuario.pack(side="left")

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack(pady=5)

        self.senha_label = Label(self.janela4, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela4, width=30)
        self.senha["show"] = "*"
        self.senha.pack(side="left")

        self.janela10 = Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack()

        self.autentic = Label(self.janela10, text="")
        self.autentic["font"] = ("Verdana", "10", "italic", "bold")
        self.autentic.pack()

        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack()

        self.botao = Button(self.janela11, width=10)
        self.botao["text"] = "Inserir"
        self.botao["command"] = self.inserirUsuario
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10)
        self.botao2["text"] = "Alterar"
        self.botao2["command"] = self.alterarUsuario
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10)
        self.botao3["text"] = "Excluir"
        self.botao3["command"] = self.excluirUsuario
        self.botao3.pack(side="left")

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        self.autentic["text"] = user.selectUser(idusuario)
        self.idusuario.delete(0, END)
        self.idusuario.insert(INSERT, user.idusuario)
        self.nome.delete(0, END)
        self.nome.insert(INSERT, user.nome)
        self.telefone.delete(0, END)
        self.telefone.insert(INSERT, user.telefone)
        self.email.delete(0, END)
        self.email.insert(INSERT, user.email)
        self.usuario.delete(0, END)
        self.usuario.insert(INSERT, user.usuario)
        self.senha.delete(0, END)
        self.senha.insert(INSERT, user.senha)


    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser()
        self.idusuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.updateUser()
        self.idusuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        self.autentic["text"] = user.deleteUser()

if __name__ == "_main_":
    root = Tk()
    Application(root)
    root.mainloop()