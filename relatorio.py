import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from banco import Banco

def exportar_para_pdf():
    pdf_file = "relatorio_usuario.pdf"

    with PdfPages(pdf_file) as pdf:
        fig, ax = plt.subplots()
        ax.plot([], [])
        ax.set_xlabel('informações pessoais')
        ax.set_ylabel('usuarios')
        ax.set_title('Gráfico usuarios')
        pdf.savefig(fig)

        plt.close(fig)
    print("PDF exportado com sucesso.")



root = tk.Tk()
root.title("Exportar para PDF")
botao_exportar = tk.Button(root, text="Exportar Gráfico para PDF", command=exportar_para_pdf)
botao_exportar.pack()
root.mainloop()
