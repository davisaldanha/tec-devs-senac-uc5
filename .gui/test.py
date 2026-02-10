import tkinter as tk

janela = tk.Tk()
janela.title("Lista de Supermercado")
janela.geometry("400x300")
janela.configure(bg="#D9EAD3")

itens = ["Arroz", "Feijão", "Leite", "Pão", "Ovos", "Açúcar", "Café"]

vars_check = {}
for item in itens:
    vars_check[item] = tk.IntVar()

frame_check = tk.Frame(janela, bg="#D9EAD3")
frame_check.pack(pady=10)

for item in itens:
    cb = tk.Checkbutton(frame_check, text=item, variable=vars_check[item], bg="#D9EAD3")
    cb.pack(anchor="w")

label_lista = tk.Label(janela, text="", bg="#D9EAD3", fg="black")
label_lista.pack(pady=10)

def atualizar_lista():
    selecionados = [item for item, var in vars_check.items() if var.get() == 1]
    if selecionados:
        label_lista.config(text="Itens selecionados: " + ", ".join(selecionados), font=('Helvetica'))
    else:
        label_lista.config(text="Nenhum item selecionado", font=('Helvetica'))

    print(vars_check)

botao_atualizar = tk.Button(janela, text="Adicionar à Lista", command=atualizar_lista, font=('Helvetica'))
botao_atualizar.pack(pady=10)

janela.mainloop()