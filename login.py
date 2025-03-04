import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from Banco import Banco
from Main import MainMenu as Mainform

class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Login")

        img = Image.open("imagem2.0.jpg")
        img = img.resize((200, 200))

        self.photo = ImageTk.PhotoImage(img)

        self.image_label = Label(self.master, image=self.photo)
        self.image_label.pack(pady=20, padx=20)

        self.janela40 = Frame(master)
        self.janela40["padx"] = 20
        self.janela40.pack()

        self.usuario_label = Label(self.janela40, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = Entry(self.janela40, width=20)
        self.usuario.pack(side="left")

        self.janela41 = Frame(master)
        self.janela41["padx"] = 20
        self.janela41.pack()

        self.senha_label = Label(self.janela41, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela41, width=20, show="*")  # Oculta o texto da senha
        self.senha.pack(side="left")

        self.janela42 = Frame(master)
        self.janela42["padx"] = 20
        self.janela42.pack()

        self.botao10 = Button(self.janela42, width=10, text="Login", command=self.entrar)
        self.botao10.pack(side="left")

    def entrar(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        banco = Banco()
        cursor = banco.conexao.cursor()

        # Verificando se o usuário e a senha estão corretos
        cursor.execute("SELECT * FROM tbl_usuarios WHERE usuario=? AND senha=?", (usuario, senha))
        engual = cursor.fetchone()

        if engual:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.abrir()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
        cursor.close()

    def abrir(self):
        # Fecha a janela de login
        self.master.destroy()
        # Abre a janela principal do menu
        root = tk.Tk()
        root.state("zoomed")
        app = Mainform(master=root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.state("zoomed")
    app = Login(master=root)
    root.mainloop()
