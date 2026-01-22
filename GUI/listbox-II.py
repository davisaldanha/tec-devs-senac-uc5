'''Widget Listbox com seleções múltiplas'''

import tkinter as tk
from tkinter.messagebox import showinfo

janela = tk.Tk()
janela.title("Exemplo de Frame")
janela.geometry("400x300")

def on_select(event):
    #recuperar o widget que disparou o evento
    listbox = event.widget

    #pegar os índeces selecionados
    indexes = listbox.curselection()

    #pegar os valores correspondente
    valores = [listbox.get(i) for i in indexes]

    label.config(text=f'Selecionado: {', '.join(valores)}')

#Widget Listbox
listbox = tk.Listbox(janela, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

#adicionando itens no listbox
for item in ['Java', 'Python', 'C++', 'Shell Script', 'Typescript', 'Ruby', 'Swift']:
    listbox.insert(tk.END, item)

#associar o evento <<ListboxSelect>> à função on_select
listbox.bind('<<ListboxSelect>>', on_select)

#label para mostrar o resultado
label = tk.Label(janela, text='Selecione um item')
label.pack(pady=10)

janela.mainloop()