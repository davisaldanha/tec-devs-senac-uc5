import tkinter as tk
from tkinter.messagebox import showinfo

janela = tk.Tk()
janela.title("Exemplo de Frame")
janela.geometry("400x300")

def new_archive():
    showinfo('Novo', 'Criar um novo arquivo...')

def open_archive():
    showinfo('Abrir', 'Abrir um arquivo existente...')

def exit():
    janela.quit()

menu_bar = tk.Menu(janela)

menu_archive = tk.Menu(menu_bar, tearoff=0)
menu_archive.add_command(label='Novo', command=new_archive)
menu_archive.add_command(label='Abrir', command=open_archive)
menu_archive.add_separator()
menu_archive.add_command(label='Sair', command=exit)

menu_bar.add_cascade(label='Arquivo', menu=menu_archive)

menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label='Sobre', command=lambda: showinfo('Sobre', 'Exemplo de Menus com Tkinter'))
menu_bar.add_cascade(label='Ajuda', menu=menu_help)

janela.config(menu=menu_bar)

janela.mainloop()