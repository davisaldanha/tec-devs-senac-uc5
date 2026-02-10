'''
Crie uma janela com alguns elementos widgets e um menu com a possibilidade
de aumentar a fonte e diminuir a fonte do texto da janela. 
Aumentar ou diminuir de 5px em 5px
Configurar o uso do Ctrl+ e Ctrl-
'''

import tkinter as tk
from tkinter import font
from tkinter import messagebox

# Função para aumentar o tamanho da fonte
def aumentar_fonte(event=None):
    tamanho_atual = fonte_texto['size']
    nova_tamanho = tamanho_atual + 5
    fonte_texto.configure(size=nova_tamanho)
    texto.config(font=fonte_texto)
    messagebox.showinfo("Aumentar Fonte", f"Tamanho da fonte aumentado para {nova_tamanho}px")

# Função para diminuir o tamanho da fonte
def diminuir_fonte(event=None):
    tamanho_atual = fonte_texto['size']
    nova_tamanho = max(5, tamanho_atual - 5) # Evitar tamanho negativo ou zero
    fonte_texto.configure(size=nova_tamanho)
    texto.config(font=fonte_texto)
    messagebox.showinfo("Diminuir Fonte", f"Tamanho da fonte diminuído para {nova_tamanho}px")

#Criando a janela principal
root = tk.Tk()
root.title("Ajuste de Fonte com Tkinter")
root.geometry('400x300')

# Criando a fonte inicial
fonte_texto = font.Font(family="Helvetica", size=12)

#Criando o menu de contexto
menu_contexto = tk.Menu(root, tearoff=0)
menu_contexto.add_command(label="Aumentar Fonte", command=aumentar_fonte)
menu_contexto.add_command(label="Diminuir Fonte", command=diminuir_fonte)

#Função para exibir o menu de contexto
def mostrar_menu(event):
    menu_contexto.tk_popup(event.x_root, event.y_root)

#Associando o clique direito ao menu
root.bind('<Button-3>', mostrar_menu)

# Associando os atalhos de teclado
root.bind('<Control-plus>', aumentar_fonte)
root.bind('<Control-minus>', diminuir_fonte)

# Um widget para testar
texto = tk.Text(root, height=10, width=40, font=fonte_texto)
texto.pack(pady=20)

# Listbox para testar
listbox = tk.Listbox(root, font=fonte_texto)
listbox.pack(pady=10)

for i in range(1, 6):
    listbox.insert(tk.END, f"Item {i}")

root.mainloop()