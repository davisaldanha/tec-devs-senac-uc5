import tkinter as tk
from tkinter.messagebox import showinfo

janela = tk.Tk()
janela.title("Exemplo de Frame")
janela.geometry("400x300")

frame_box = tk.Frame(janela, bg="#444444", padx=10, pady=10)

list_box = tk.Listbox(frame_box, height=4, width=30, selectmode=tk.SINGLE)
list_box.pack(pady=10, side=tk.LEFT)

for item in ['Java', 'Python', 'C++', 'Shell Script', 'Typescript', 'Ruby', 'Swift']:
    list_box.insert(tk.END, item)

def mostrar_selecao_listbox(event):
    selecao = list_box.curselection()

    showinfo(
        title='Seleção da ListBox',
        message=f'Stack selecionada: {list_box.get(selecao[0])}'
    )

list_box.bind('<<ListboxSelect>>', mostrar_selecao_listbox)


scrollbar = tk.Scrollbar(frame_box, orient=tk.VERTICAL, command=list_box.yview)

frame_box.pack(pady=20)


janela.mainloop()