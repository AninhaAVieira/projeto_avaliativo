from tkinter import *
from tkinter import ttk, messagebox
from apliClientes import Clientes
import tkinter as tk
from tkinter import Frame, Button, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

class Cliente:
    def __init__(self, master=None):
        self.master = master
        self.janela21 = Frame(master)
        self.janela21.pack()
        self.msg1 = Label(self.janela21, text="Informe os dados do Cliente:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        self.janela22 = Frame(master)
        self.janela22["padx"] = 20
        self.janela22.pack()

        self.idcliente_label = Label(self.janela22, text="ID Cliente:")
        self.idcliente_label.pack(side="left")
        self.idcliente = Entry(self.janela22, width=20)
        self.idcliente.pack(side="left")

        self.busca = Button(self.janela22, text="Buscar", command=self.buscarCliente)
        self.busca.pack()

        self.janela23 = Frame(master)
        self.janela23["padx"] = 20
        self.janela23.pack()

        self.nome_label = Label(self.janela23, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela23, width=30)
        self.nome.pack(side="left")

        # Adicionando a Combobox para selecionar a cidade
        self.janela24 = Frame(master)
        self.janela24["padx"] = 20
        self.janela24.pack()

        self.cidade_label = Label(self.janela24, text="Cidade:")
        self.cidade_label.pack(side="left")
        self.cidade_combobox = ttk.Combobox(self.janela24, width=27)
        self.cidade_combobox.pack(side="left")
        self.carregarCidades()  # Carregar cidades na Combobox

        self.janela25 = Frame(master)
        self.janela25["padx"] = 20
        self.janela25.pack(pady=5)

        self.nascimento_label = Label(self.janela25, text="Nascimento:")
        self.nascimento_label.pack(side="left")
        self.nascimento = Entry(self.janela25, width=28)
        self.nascimento.pack(side="left")

        self.janela26 = Frame(master)
        self.janela26["padx"] = 20
        self.janela26.pack()

        self.cpf_label = Label(self.janela26, text="CPF:")
        self.cpf_label.pack(side="left")
        self.cpf = Entry(self.janela26, width=30)
        self.cpf.pack(side="left")

        self.janela27 = Frame(master)
        self.janela27["padx"] = 20
        self.janela27.pack()

        self.genero_label = Label(self.janela27, text="Gênero:")
        self.genero_label.pack(side="left")
        self.genero = Entry(self.janela27, width=30)
        self.genero.pack(side="left")

        self.janela28 = Frame(master)
        self.janela28["padx"] = 20
        self.janela28.pack()

        self.autentic = Label(self.janela28, text="", font=("Verdana", "10", "italic", "bold"))
        self.autentic.pack()

        # Adicionando os botões para Inserir, Alterar e Excluir
        self.janela11 = Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack(pady=5)

        self.botao = Button(self.janela11, width=10, text="Inserir", command=self.inserirCliente)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela11, width=10, text="Alterar", command=self.alterarCliente)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela11, width=10, text="Excluir", command=self.excluirCliente)
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

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Nome", "Nascimento", "CPF", "Gênero", "Cidade"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Nascimento", text="Nascimento")
        self.tree.heading("CPF", text="CPF")
        self.tree.heading("Gênero", text="Gênero")
        self.tree.heading("Cidade", text="Cidade")
        self.tree.pack()

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

        # Bind da função para preencher entradas com seleção do Treeview
        self.tree.bind('<<TreeviewSelect>>', self.preencher_entries)

    def carregarCidades(self):
        cli = Clientes()
        cidades = cli.selectCidades()
        self.cidade_combobox['values'] = cidades

    def atualizarTabela(self):
        cli = Clientes()
        clientes = cli.selectAllClientes()
        self.tree.delete(*self.tree.get_children())
        for c in clientes:
            self.tree.insert("", "end", values=(c[0], c[1], c[2], c[3], c[4], c[5]))

    def buscarCliente(self):
        cli = Clientes()
        idcliente = self.idcliente.get()
        self.autentic["text"] = cli.selectCliente(idcliente)
        self.idcliente.delete(0, END)
        self.idcliente.insert(INSERT, cli.idcliente)
        self.nome.delete(0, END)
        self.nome.insert(INSERT, cli.nome)
        self.nascimento.delete(0, END)
        self.nascimento.insert(INSERT, cli.nascimento)
        self.cpf.delete(0, END)
        self.cpf.insert(INSERT, cli.cpf)
        self.genero.delete(0, END)
        self.genero.insert(INSERT, cli.genero)
        self.cidade_combobox.set(cli.cidade)

    def inserirCliente(self):
        resposta = messagebox.askokcancel("Confirmar Cadastro", "Deseja realmente inserir este cliente?")
        if resposta:
            cli = Clientes(nome=self.nome.get(), nascimento=self.nascimento.get(), cpf=self.cpf.get(), genero=self.genero.get(), cidade=self.cidade_combobox.get())
            result = cli.insertCliente()
            messagebox.showinfo("Resultado", result)
            self.atualizarTabela()

    def alterarCliente(self):
        resposta = messagebox.askokcancel("Confirmar Alteração", "Deseja realmente alterar este cliente?")
        if resposta:
            cli = Clientes(idcliente=self.idcliente.get(), nome=self.nome.get(), nascimento=self.nascimento.get(), cpf=self.cpf.get(), genero=self.genero.get(), cidade=self.cidade_combobox.get())
            result = cli.updateCliente()
            messagebox.showinfo("Resultado", result)
            self.atualizarTabela()

    def excluirCliente(self):
        resposta = messagebox.askokcancel("Confirmar Exclusão", "Deseja realmente excluir este cliente?")
        if resposta:
            cli = Clientes(idcliente=self.idcliente.get())
            result = cli.deleteCliente()
            messagebox.showinfo("Resultado", result)
            self.atualizarTabela()

    def preencher_entries(self, event):
        try:
            item = self.tree.selection()[0]  # Pega o item selecionado
            dados = self.tree.item(item, 'values')  # Obtém os valores do item

            # Preenche os campos de entrada com os dados
            self.idcliente.delete(0, END)
            self.idcliente.insert(0, dados[0])
            self.nome.delete(0, END)
            self.nome.insert(0, dados[1])
            self.nascimento.delete(0, END)
            self.nascimento.insert(0, dados[2])
            self.cpf.delete(0, END)
            self.cpf.insert(0, dados[3])
            self.genero.delete(0, END)
            self.genero.insert(0, dados[4])
            self.cidade_combobox.set(dados[5])
        except IndexError:
            pass  # Nenhum item selecionado

    def voltar(self):
        self.master.destroy()

    def gerar_relatorio(self):
        cli = Clientes()
        clientes = cli.selectAllClientes()

        c = canvas.Canvas("relatorio_clientes.pdf", pagesize=letter)
        width, height = letter

        c.drawString(1 * inch, height - 1 * inch, "Relatório de Clientes")
        y = height - 1.5 * inch

        for cliente in clientes:
            c.drawString(1 * inch, y, f"ID: {cliente[0]}, Nome: {cliente[1]}, Nascimento: {cliente[2]}, CPF: {cliente[3]}, Gênero: {cliente[4]}, Cidade: {cliente[5]}")
            y -= 0.3 * inch

        c.save()
        messagebox.showinfo("Relatório", "Relatório de clientes gerado com sucesso!")

if __name__ == "__main__":
    app = Cliente()
    app.mainloop()
