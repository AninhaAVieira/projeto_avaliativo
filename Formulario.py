import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Usuarios import *
import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from Banco import Banco

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha) VALUES (?, ?, ?, ?, ?)",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {e}"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("UPDATE tbl_usuarios SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? WHERE idusuario = ?",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {e}"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_usuarios WHERE idusuario = ?", (self.idusuario,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {e}"

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios WHERE idusuario = ?", (idusuario,))
            linha = c.fetchone()
            if linha:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
                c.close()
                return "Busca feita com sucesso!"
            else:
                c.close()
                return "Usuário não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {e}"

    def selectAllUsers(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios")
            linhas = c.fetchall()
            c.close()
            return linhas
        except Exception as e:
            return f"Ocorreu um erro na recuperação dos usuários: {e}"

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Usuários")

        # Frame para o formulário
        self.janela1 = tk.Frame(master)
        self.janela1.pack(padx=10, pady=10)

        # Título
        self.msg1 = tk.Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("Verdana", "14", "bold")
        self.msg1.pack()

        # Frame para a busca
        self.janela2 = tk.Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = tk.Label(self.janela2, text="Id usuário:")
        self.idusuario_label.pack(side="left")
        self.idusuario = tk.Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = tk.Button(self.janela2, text="Buscar", command=self.buscarUsuario)
        self.busca.pack()

        # Frames para os campos de dados
        self.janela3 = tk.Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = tk.Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = tk.Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = tk.Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.telefone_label = tk.Label(self.janela5, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = tk.Entry(self.janela5, width=28)
        self.telefone.pack(side="left")

        self.janela6 = tk.Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.email_label = tk.Label(self.janela6, text="E-mail:")
        self.email_label.pack(side="left")
        self.email = tk.Entry(self.janela6, width=30)
        self.email.pack(side="left")

        self.janela7 = tk.Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack(pady=5)

        self.usuario_label = tk.Label(self.janela7, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = tk.Entry(self.janela7, width=29)
        self.usuario.pack(side="left")

        self.janela4 = tk.Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack(pady=5)

        self.senha_label = tk.Label(self.janela4, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = tk.Entry(self.janela4, width=30, show="*")
        self.senha.pack(side="left")

        # Frame para os botões
        self.janela10 = tk.Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack()

        self.janela11 = tk.Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack()

        self.botao = tk.Button(self.janela11, width=10, text="Inserir", command=self.inserirUsuario)
        self.botao.pack(side="left")

        self.botao2 = tk.Button(self.janela11, width=10, text="Alterar", command=self.alterarUsuario)
        self.botao2.pack(side="left")

        self.botao3 = tk.Button(self.janela11, width=10, text="Excluir", command=self.excluirUsuario)
        self.botao3.pack(side="left")

        # Adicionando o botão "Voltar"
        self.botao_voltar = tk.Button(self.janela11, width=10, text="Voltar", command=self.voltar)
        self.botao_voltar.pack(side="left")

        # Adicionando o botão para gerar relatório PDF
        self.botao_relatorio = tk.Button(self.janela11, width=15, text="Gerar Relatório", command=self.gerar_relatorio)
        self.botao_relatorio.pack(side="left")

        # Frame para a tabela
        self.janela12 = tk.Frame(master)
        self.janela12["padx"] = 20
        self.janela12.pack(pady=10)

        self.tree = ttk.Treeview(self.janela12, columns=("ID", "Nome", "Telefone", "E-mail", "Usuário"),
                                 show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Usuário", text="Usuário")
        self.tree.pack()

        # Atualiza a tabela quando a aplicação é carregada
        self.atualizarTabela()

        # Bind da função para preencher entradas com seleção do Treeview
        self.tree.bind('<<TreeviewSelect>>', self.preencher_entries)

    def atualizarTabela(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert("", "end", values=(u[0], u[1], u[2], u[3], u[4]))

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        result = user.selectUser(idusuario)
        messagebox.showinfo("Resultado da Busca", result)
        if "não encontrado" not in result:
            self.idusuario.delete(0, tk.END)
            self.idusuario.insert(tk.INSERT, user.idusuario)
            self.nome.delete(0, tk.END)
            self.nome.insert(tk.INSERT, user.nome)
            self.telefone.delete(0, tk.END)
            self.telefone.insert(tk.INSERT, user.telefone)
            self.email.delete(0, tk.END)
            self.email.insert(tk.INSERT, user.email)
            self.usuario.delete(0, tk.END)
            self.usuario.insert(tk.INSERT, user.usuario)
            self.senha.delete(0, tk.END)
            self.senha.insert(tk.INSERT, user.senha)

            # Atualiza a tabela com o usuário encontrado
            self.atualizarTabela()

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        result = user.insertUser()
        messagebox.showinfo("Resultado da Inserção", result)
        self.limparCampos()
        self.atualizarTabela()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        result = user.updateUser()
        messagebox.showinfo("Resultado da Alteração", result)
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        result = user.deleteUser()
        messagebox.showinfo("Resultado da Exclusão", result)
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.idusuario.delete(0, tk.END)
        self.nome.delete(0, tk.END)
        self.telefone.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.usuario.delete(0, tk.END)
        self.senha.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())

    def preencher_entries(self, event):
        try:
            item = self.tree.selection()[0]  # Pega o item selecionado
            dados = self.tree.item(item, 'values')  # Obtém os valores do item

            # Preenche os campos de entrada com os dados
            self.idusuario.delete(0, tk.END)
            self.idusuario.insert(0, dados[0])
            self.nome.delete(0, tk.END)
            self.nome.insert(0, dados[1])
            self.telefone.delete(0, tk.END)
            self.telefone.insert(0, dados[2])
            self.email.delete(0, tk.END)
            self.email.insert(0, dados[3])
            self.usuario.delete(0, tk.END)
            self.usuario.insert(0, dados[4])
            self.senha.delete(0, tk.END)
            # Não é recomendado mostrar senhas em texto claro. Considere uma abordagem diferente para a segurança.
        except IndexError:
            pass  # Nenhum item selecionado

    def voltar(self):
        self.master.destroy()

    def gerar_relatorio(self):
        user = Usuarios()
        usuarios = user.selectAllUsers()

        c = canvas.Canvas("relatorio_usuarios.pdf", pagesize=letter)
        width, height = letter

        c.drawString(1 * inch, height - 1 * inch, "Relatório de Usuários")
        y = height - 1.5 * inch

        for u in usuarios:
            c.drawString(1 * inch, y, f"ID: {u[0]}, Nome: {u[1]}, Telefone: {u[2]}, E-mail: {u[3]}, Usuário: {u[4]}")
            y -= 0.3 * inch

        c.save()
        messagebox.showinfo("Relatório", "Relatório de usuários gerado com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

