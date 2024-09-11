import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from banco import Banco

def obter_dados_usuarios():
    banco = Banco()
    return banco.py()

def exportar_para_pdf():
    try:
        dados = obter_dados_usuarios()


        if not dados:
            messagebox.showwarning("Aviso", "Nenhum dado encontrado para exportar.")
            return

        pdf_file = "relatorio_usuario.pdf"

        with PdfPages(pdf_file) as pdf:
            fig, ax = plt.subplots()


            table_data = [["Nome", "E-mail", "Cidade", "Telefone"]] + dados
            table = ax.table(cellText=table_data, colLabels=None, loc='center', cellLoc='center', bbox=[0, 0, 1, 1])
            table.auto_set_font_size(False)
            table.set_fontsize(10)
            ax.axis('off')

            plt.title('Relatório de Usuários')
            pdf.savefig(fig)

            plt.close(fig)

        messagebox.showinfo("Sucesso", "PDF exportado com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")


root = tk.Tk()
root.title("Exportar Relatório para PDF")

botao_exportar = tk.Button(root, text="Exportar Relatório para PDF", command=exportar_para_pdf)
botao_exportar.pack(pady=20)

root.mainloop()
