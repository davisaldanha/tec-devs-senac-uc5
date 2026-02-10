import tkinter as tk
from tkinter import messagebox

#Copiar texto selecionado
def copiar(event=None):
    try:
        selected_text = texto.selection_get()
        texto.clipboard_clear()
        texto.clipboard_append(selected_text)
        messagebox.showinfo("Copiar", "Texto copiado!")
    except tk.TclError:
        messagebox.showwarning("Copiar", "Nenhum texto selecionado!")
    return "break"

def colar(event=None):
    try:
        clipboard_text = texto.clipboard_get()
        texto.insert(tk.INSERT, clipboard_text)
        messagebox.showinfo("Colar", "Texto colado!")
    except tk.TclError:
        messagebox.showwarning("Colar", "Área de transferência vazia!")
    return "break" # impede o comportamento padrão

def cortar(event=None):
    try:
        selected_text = texto.selection_get()
        texto.clipboard_clear()
        texto.clipboard_append(selected_text)
        texto.delete(tk.SEL_FIRST, tk.SEL_LAST)
        messagebox.showinfo("Cortar", "Texto cortado!")
    except tk.TclError:
        messagebox.showwarning("Cortar", "Nenhum texto selecionado!")
    return "break"

# Criando a janela principal
root = tk.Tk()
root.title("Menu de Contexto + Atalhos")
root.geometry("400x300")

# Criando o menu de contexto
menu_contexto = tk.Menu(root, tearoff=0)
menu_contexto.add_command(label="Copiar", command=copiar, accelerator="Ctrl+C")
menu_contexto.add_command(label="Colar", command=colar, accelerator="Ctrl+V")
menu_contexto.add_command(label="Cortar", command=cortar, accelerator="Ctrl+X")

# Função para exibir o menu de contexto
def mostrar_menu(event):
    menu_contexto.tk_popup(event.x_root, event.y_root)

# Associando o clique direito ao menu
root.bind("<Button-3>", mostrar_menu)

# Um widget para testar
texto = tk.Text(root, height=10, width=40)
texto.pack(pady=20)

# Associando atalhos de teclado ao widget de texto
texto.bind("<Control-c>", copiar)
texto.bind("<Control-v>", colar)
texto.bind("<Control-x>", cortar)

root.mainloop()