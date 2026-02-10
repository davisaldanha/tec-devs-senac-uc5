import tkinter as tk
from tkinter import messagebox

#Copiar texto selecionado
def copiar():
    # Gerar evento de cópia
    texto.event_generate("<<Copy>>")
    messagebox.showinfo("Copiar", "Texto copiado!")

def colar():
    # Gerar evento de colar
    texto.event_generate("<<Paste>>")
    messagebox.showinfo("Colar", "Texto colado!")

def cortar():
    # Gerar evento de cortar
    texto.event_generate("<<Cut>>")
    messagebox.showinfo("Cortar", "Texto cortado!")

# Criando a janela principal
root = tk.Tk()
root.title("Menu de Contexto com Tkinter")
root.geometry("400x300")

# Criando o menu de contexto
menu_contexto = tk.Menu(root, tearoff=0)
menu_contexto.add_command(label="Copiar", command=copiar)
menu_contexto.add_command(label="Colar", command=colar)
menu_contexto.add_command(label="Cortar", command=cortar)

# Função para exibir o menu de contexto
def mostrar_menu(event):
    menu_contexto.tk_popup(event.x_root, event.y_root)

# Associando o clique direito ao menu
root.bind("<Button-3>", mostrar_menu)

# Um widget para testar
texto = tk.Text(root, height=10, width=40)
texto.pack(pady=20)

root.mainloop()