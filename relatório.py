from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from Clientes import Clientes
from Usuarios import Usuarios
from Cidade import Cidade

def gerar_pdf_clientes():
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

def gerar_pdf_usuarios():
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

def gerar_pdf_cidades():
    cid = Cidade()
    cidades = cid.selectCidades()

    c = canvas.Canvas("relatorio_cidades.pdf", pagesize=letter)
    width, height = letter

    c.drawString(1 * inch, height - 1 * inch, "Relatório de Cidades")
    y = height - 1.5 * inch

    for cidade in cidades:
        c.drawString(1 * inch, y, f"Cidade: {cidade}")
        y -= 0.3 * inch

    c.save()

if __name__ == "__main__":
    gerar_pdf_clientes()
    gerar_pdf_usuarios()
    gerar_pdf_cidades()
    print("Relatórios gerados com sucesso!")
