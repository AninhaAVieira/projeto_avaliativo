import tkinter as tk
from tkinter import Menu
from Formulario import Application as UserForm
from Cidade import Cidade as Cidform  # Certifique-se de que a classe Cidade está definida e importada
from Clientes import Cliente as Cliform  # Certifique-se de que a classe Cliente está definida e importada

class MainMenu:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Sistema de Gestão")

        # Criar a barra de menus
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Criar o menu "Sistema"
        self.system_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Sistema", menu=self.system_menu)
        self.system_menu.add_command(label="Usuários", command=self.open_user_screen)
        self.system_menu.add_command(label="Cidades", command=self.open_city_screen)
        self.system_menu.add_command(label="Clientes", command=self.open_client_screen)
        self.system_menu.add_separator()
        self.system_menu.add_command(label="Sair", command=self.master.quit)

    def open_user_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = UserForm(self.new_window)

    def open_city_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Cidform(self.new_window)

    def open_client_screen(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = Cliform(self.new_window)

if __name__ == "__main__":
    root = tk.Tk()
    root.state("zoomed")
    app = MainMenu(master=root)
    root.mainloop()
