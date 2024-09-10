from tkinter import *
from tkinter import ttk, messagebox
from apliCidade import Cidades
from Banco import Banco
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


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

        # Adicionando o botão Voltar
        self.botao_voltar = Button(self.janela11, width=10, text="Voltar", command=self.voltar)
        self.botao_voltar.pack(side="left")

        # Botão para gerar o relatório PDF
        self.botao_relatorio = Button(self.janela11, width=15, text="Gerar Relatório", command=self.gerar_relatorio)
        self.botao_relatorio.pack(side="left")

        # Frame para a tabela
        self.janela12 = Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Cidade", "UF"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.heading("UF", text="UF")
        self.tree.pack()

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

        # Bind da função para preencher entradas com seleção do Treeview
        self.tree.bind('<<TreeviewSelect>>', self.preencher_entries)

    def atualizarTabela(self):
        cid = Cidades()
        cidades = cid.selectAllCidades()
        self.tree.delete(*self.tree.get_children())
        for c in cidades:
            self.tree.insert("", "end", values=(c[0], c[1], c[2]))

    def buscarCidade(self):
        cid = Cidades()
        idcidade = self.idcidade.get()
        dados = cid.selectCidade(idcidade)
        if dados:
            self.idcidade.delete(0, END)
            self.idcidade.insert(INSERT, dados[0])
            self.cidade.delete(0, END)
            self.cidade.insert(INSERT, dados[1])
            self.uf.delete(0, END)
            self.uf.insert(INSERT, dados[2])
        else:
            messagebox.showinfo("Resultado da Busca", "Cidade não encontrada.")
        self.idcidade.delete(0, END)

    def inserirCidade(self):
        cid = Cidades(cidade=self.cidade.get(), uf=self.uf.get())
        result = cid.insertCidade()
        messagebox.showinfo("Resultado da Inserção", result)
        self.atualizarTabela()

    def alterarCidade(self):
        cid = Cidades(idcidade=self.idcidade.get(), cidade=self.cidade.get(), uf=self.uf.get())
        result = cid.updateCidade()
        messagebox.showinfo("Resultado da Alteração", result)
        self.atualizarTabela()

    def excluirCidade(self):
        cidade = self.cidade.get()

        banco = Banco()
        cursor = banco.conexao.cursor()

        cursor.execute("SELECT * FROM tbl_clientes WHERE cidade = ?", (cidade,))
        cadastrada = cursor.fetchone()

        if cadastrada:
            messagebox.showerror("Erro", "Cidade não pode ser excluída pois está cadastrada em clientes")
        else:
            cid = Cidades(idcidade=self.idcidade.get())
            result = cid.deleteCidade()
            if result:
                messagebox.showinfo("Excluir", "Cidade excluída com sucesso!")
            else:
                messagebox.showerror("Erro", "Erro ao excluir cidade.")
            self.atualizarTabela()

        cursor.close()

    def preencher_entries(self, event):
        try:
            item = self.tree.selection()[0]  # Pega o item selecionado
            dados = self.tree.item(item, 'values')  # Obtém os valores do item

            # Preenche os campos de entrada com os dados
            self.idcidade.delete(0, END)
            self.idcidade.insert(0, dados[0])
            self.cidade.delete(0, END)
            self.cidade.insert(0, dados[1])
            self.uf.delete(0, END)
            self.uf.insert(0, dados[2])
        except IndexError:
            pass  # Nenhum item selecionado

    def voltar(self):
        # Limpar campos de entrada e atualizar a tabela
        self.idcidade.delete(0, END)
        self.cidade.delete(0, END)
        self.uf.delete(0, END)
        self.atualizarTabela()

    def voltar(self):
        self.master.destroy()

    def gerar_relatorio(self):
        cid = Cidades()
        cidades = cid.selectAllCidades()

        c = canvas.Canvas("relatorio_cidade.pdf", pagesize=letter)
        width, height = letter

        c.drawString(1 * inch, height - 1 * inch, "Relatório de Cidades")
        y = height - 1.5 * inch

        for cidade in cidades:
            c.drawString(1 * inch, y, f"ID: {cidade[0]}, Cidade: {cidade[1]}, UF: {cidade[2]}")
            y -= 0.3 * inch

        c.save()
        messagebox.showinfo("Relatório", "Relatório de cidades gerado com sucesso!")


if __name__ == "__main__":
    root = Tk()
    app = Cidade(master=root)
    app.mainloop()
