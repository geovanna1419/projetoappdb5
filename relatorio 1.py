import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from banco import Banco
import pandas as pd


def exportar_para_pdf():
    pdf_file = "relatorio_usuarios.pdf"


    banco = Banco()
    cursor = banco.conexao.cursor()
    cursor.execute("SELECT nome, idade from banco ")
    dados = cursor.fetchall()
    cursor.close()
    banco.conexao.close()


    df = pd.DataFrame(dados, columns=['Nome', 'Idade'])


    idade_counts = df['Idade'].value_counts().sort_index()

    fig, ax = plt.subplots()
    idade_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('Idade')
    ax.set_ylabel('Número de Usuários')
    ax.set_title('Distribuição de Idades dos Usuários')


    with PdfPages(pdf_file) as pdf:
        pdf.savefig(fig)

    plt.close(fig)
    print("PDF exportado com sucesso.")



root = tk.Tk()
root.title("Exportar Relatório para PDF")
botao_exportar = tk.Button(root, text="Exportar Relatório para PDF", command=exportar_para_pdf)
botao_exportar.pack()
root.mainloop()
