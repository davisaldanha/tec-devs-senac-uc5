'''Widget Listbox com duplo click '''

import tkinter as tk
from tkinter.messagebox import showinfo

janela = tk.Tk()
janela.title("Exemplo de Frame")
janela.geometry("400x300")

def on_double_click(event):
    #recuperar o widget que disparou o evento
    listbox = event.widget

    #pegar os índeces selecionados
    indexes = listbox.curselection()

    if indexes:
        valor = listbox.get(indexes[0])
        label.config(text=f'Selecionado: {valor}')
        print('!')

#Widget Listbox
listbox = tk.Listbox(janela)
listbox.pack(pady=10)

#adicionando itens no listbox
for item in ['Java', 'Python', 'C++', 'Shell Script', 'Typescript', 'Ruby', 'Swift']:
    listbox.insert(tk.END, item)

#associar o evento <<ListboxSelect>> à função on_select
listbox.bind('<Double-Button-1>', on_double_click)

#label para mostrar o resultado
label = tk.Label(janela, text='Selecione um item com duplo clique!')
label.pack(pady=10)

janela.mainloop()