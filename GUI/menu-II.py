import tkinter as tk
from tkinter.messagebox import showinfo

janela = tk.Tk()
janela.title("Exemplo de Frame")
janela.geometry("400x300")

def copy():
    texto.event_generate("<<Copy>>")
    showinfo('Copiar', 'Texto Copiado!')

def paste():
    texto.event_generate("<<Paste>>")
    showinfo('Colar', 'Texto Colado!')

def cut():
    texto.event_generate("<<Cut>>")
    showinfo('Cortar', 'Texto Cortado!')

menu_context = tk.Menu(janela, tearoff=0)
menu_context.add_command(label='Copiar', command=copy)
menu_context.add_command(label='Colar', command=paste)
menu_context.add_command(label='Cortar', command=cut)

def show_menu(event):
    menu_context.tk_popup(event.x_root, event.y_root)

janela.bind('<Button-3>', show_menu)

texto = tk.Text(janela, height=10, width=40)
texto.pack(pady=20)

janela.mainloop()
