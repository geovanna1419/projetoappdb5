import tkinter as tk
from tkinter import *
from usuario import Usuarios

class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Gerenciamento de Usuários")
        self.fontePadrao = ("Arial", "12")


        self.janela = Frame(master)
        self.janela.pack(padx=10, pady=10)


        self.titulo = Label(self.janela, text="Informe os dados")
        self.titulo["font"] = ("Arial", "29", "bold")
        self.titulo.pack()


        self.janela2 = Frame(master, padx=20)
        self.janela2.pack()
        self.janela3 = Frame(master, padx=20)
        self.janela3.pack()
        self.janela4 = Frame(master, padx=20)
        self.janela4.pack()
        self.janela5 = Frame(master, padx=20)
        self.janela5.pack()
        self.janela6 = Frame(master, padx=20)
        self.janela6.pack()
        self.janela7 = Frame(master, padx=20)
        self.janela7.pack()
        self.janela8 = Frame(master, padx=20)
        self.janela8.pack()


        self.nomeLabel = Label(self.janela2, text="ID Usuário", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.idusuario = Entry(self.janela2, width=30, font=self.fontePadrao)
        self.idusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.janela2, text="Buscar", font=("Calibri", "8"), width=10, command=self.buscarUsuario)
        self.btnBuscar.pack(side=LEFT)

        self.nomeLabel = Label(self.janela3, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3, width=30, font=self.fontePadrao)
        self.nome.pack(side=LEFT)

        self.numeroLabel = Label(self.janela4, text="Telefone", font=self.fontePadrao)
        self.numeroLabel.pack(side=LEFT)
        self.telefone = Entry(self.janela4, width=30, font=self.fontePadrao)
        self.telefone.pack(side=LEFT)

        self.emailLabel = Label(self.janela5, text="E-mail", font=self.fontePadrao)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5, width=30, font=self.fontePadrao)
        self.email.pack(side=LEFT)

        self.usuarioLabel = Label(self.janela6, text="Usuário", font=self.fontePadrao)
        self.usuarioLabel.pack(side=LEFT)
        self.usuario = Entry(self.janela6, width=30, font=self.fontePadrao)
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.janela7, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7, width=30, font=self.fontePadrao, show="*")
        self.senha.pack(side=LEFT)


        self.bntInsert = Button(self.janela8, text="Inserir", font=("Calibri", "8"), width=20, command=self.inserirUsuario)
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.janela8, text="Alterar", font=("Calibri", "8"), width=20, command=self.alterarUsuario)
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.janela8, text="Excluir", font=("Calibri", "8"), width=20, command=self.excluirUsuario)
        self.bntExcluir.pack(side=LEFT)


        self.lblmsg = Label(self.janela, text="", font=self.fontePadrao)
        self.lblmsg.pack()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        resultado = user.selectUser(idusuario)
        if resultado:
            self.nome.delete(0, END)
            self.nome.insert(0, resultado['nome'])
            self.telefone.delete(0, END)
            self.telefone.insert(0, resultado['telefone'])
            self.email.delete(0, END)
            self.email.insert(0, resultado['email'])
            self.usuario.delete(0, END)
            self.usuario.insert(0, resultado['usuario'])
            self.senha.delete(0, END)
            self.senha.insert(0, resultado['senha'])
            self.lblmsg["text"] = "Usuário encontrado"
        else:
            self.lblmsg["text"] = "Usuário não encontrado"

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        mensagem = user.insertUser()
        self.lblmsg["text"] = mensagem
        self.limparCampos()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        mensagem = user.updateUser()
        self.lblmsg["text"] = mensagem
        self.limparCampos()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        mensagem = user.deleteUser()
        self.lblmsg["text"] = mensagem
        self.limparCampos()

    def limparCampos(self):
        self.idusuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)

# Execução da interface gráfica
root = Tk()
app = Login(root)
root.mainloop()