import tkinter as tk
from tkinter import *
from banco import Banco
from tkinter import messagebox

class Login:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.janela["padx"] = 20
        self.janela["pady"] = 5
        self.janela.pack()


        self.img = PhotoImage(file="imagem/TikTok.jpg")
        self.lblimg = Label(self.janela, image=self.img)
        self.lblimg.pack()


        self.janela40 = tk.Frame(master)
        self.janela40["padx"] = 20
        self.janela40.pack()

        self.usuario_label = tk.Label(self.janela40, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = tk.Entry(self.janela40, width=20)
        self.usuario.pack(side="left")

        self.janela41 = tk.Frame(master)
        self.janela41["padx"] = 20
        self.janela41.pack()

        self.senha_label = tk.Label(self.janela41, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = tk.Entry(self.janela41, width=20, show="*")
        self.senha.pack(side="left")

        self.janela42 = tk.Frame(master)
        self.janela42["padx"] = 20
        self.janela42.pack()

        self.botao10 = tk.Button(self.janela42, width=10, text="Login", command=self.entrar)
        self.botao10.pack(side="left")
        self.new_window = None

        def entrar(self):
            usuario = self.usuario.get()
            senha = self.senha.get()

            banco = Banco()
            cursor = banco.conexao.cursor()

            cursor.execute("SELECT * FROM tbl_usuarios WHERE usuario=? AND senha=?", (usuario, senha))
            resultado = cursor.fetchone()

            if resultado:
                messagebox.showinfo("Login", "Login realizado com sucesso!")
                self.abrir()
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos!")

            cursor.close()
            banco.conexao.close()

        def abrir(self):
            if self.new_window is None or not self.new_window.winfo_exists():
                self.new_window = tk.Toplevel(self.master)
                self.new_window.title("Nova Janela")

    if __name__ == "__main__":
        print("Executando o script...")
        root = tk.Tk()
        root.state("zoomed")
        root.mainloop()