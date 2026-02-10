import tkinter as tk
from tkinter import messagebox

def novo_arquivo():
    messagebox.showinfo("Novo", "Criar um novo arquivo...")

def abrir_arquivo():
    messagebox.showinfo("Abrir", "Abrir um arquivo existente...")

def sair():
    root.quit()

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo de Menu com Tkinter")
root.geometry("400x300")

# Criando a barra de menus
menu_bar = tk.Menu(root)

# Menu Arquivo
menu_arquivo = tk.Menu(menu_bar, tearoff=0)
menu_arquivo.add_command(label="Novo", command=novo_arquivo)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_separator() # Separador no menu 
menu_arquivo.add_command(label="Sair", command=sair)
# Adicionando o menu Arquivo à barra de menus
menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo) 

# Menu Ajuda
menu_ajuda = tk.Menu(menu_bar, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=lambda: messagebox.showinfo("Sobre", "Exemplo de menus com Tkinter"))
menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

# Associando a barra de menus à janela
root.config(menu=menu_bar)

root.mainloop()