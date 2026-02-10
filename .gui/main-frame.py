import tkinter as tk
janela = tk.Tk()
janela.title("Minha Primeira GUI")
janela.geometry("400x300")

#Label
label = tk.Label(janela, text="Segunda-feira", font=("Arial", 16), bg="#75701b")
label.pack(pady=20) # Adiciona um rótulo com texto


#Frame exemplo
frame = tk.Frame(janela, bg="#333333", padx=10, pady=10, width=500, height=100)
frame.pack(pady=20)

label_frame = tk.Label(frame, text="Dentro do Frame", bg="#333333", fg="#FFFFFF")
label_frame.grid(row=0, column=0)


# Botão dentro do frame
botao_frame = tk.Button(frame, text="Botão do Frame")
botao_frame.grid(row=1, column=0, pady=10)

#Checkbutton exemplo
var_check = tk.IntVar()
checkbutton = tk.Checkbutton(janela, text="Opção", variable=var_check, bg="#75701b")
checkbutton.pack(pady=10)

#Checkar estado do checkbutton
def verificar_checkbutton():
    estado = var_check.get()
    label.config(text=f"Checkbutton está: {'Selecionado' if estado else 'Não Selecionado'}")

botao_check = tk.Button(janela, text="Verificar Checkbutton", command=verificar_checkbutton)
botao_check.pack(pady=10)

#Frame 2 exemplo
frame2 = tk.Frame(janela, bg="#555555", padx=10, pady=10)
frame2.pack(pady=20)

label_frame2 = tk.Label(frame2, text="Segundo Frame", bg="#555555", fg="#FFFFFF")
label_frame2.grid(row=0, column=0)

# Radiobuttons dentro do frame2
var_radio = tk.StringVar(value="Opção 1")
radio1 = tk.Radiobutton(frame2, text="Opção 1", variable=var_radio, value="Opção 1", bg="#555555")
radio2 = tk.Radiobutton(frame2, text="Opção 2", variable=var_radio, value="Opção 2", bg="#555555")
radio1.grid(row=1, column=0, sticky="w")
radio2.grid(row=2, column=0, sticky="w")

# Botão para mostrar a opção selecionada
def mostrar_opcao_radio():
    label.config(text=f"Selecionado: {var_radio.get()}")

botao_radio = tk.Button(janela, text="Mostrar Opção Selecionada", command=mostrar_opcao_radio)
botao_radio.pack(pady=10)

#--------------------------------------------------------------------------------------------------------

#ListBox exemplo
from tkinter.messagebox import showinfo

frame_listbox = tk.Frame(janela, bg="#444444", padx=10, pady=10)

listbox = tk.Listbox(frame_listbox, height=4, selectmode=tk.SINGLE, width=30)
listbox.pack(pady=10, side=tk.LEFT)

for item in ['Java', 'Python', 'C++', 'JavaScript', 'Ruby', 'Swift']:
    listbox.insert(tk.END, item)

def mostrar_selecao_listbox(event):
    selecao = listbox.get(tk.ACTIVE)

    showinfo(
        title="Seleção da ListBox",
        message=f"Você selecionou: {selecao}"
    )

listbox.bind('<<ListboxSelect>>', mostrar_selecao_listbox)

#Adicionar uma barra de rolagem à ListBox
scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL, command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)


scrollbar.pack(pady=10, side=tk.RIGHT, fill=tk.Y)

frame_listbox.pack(pady=20)

#Spinbox exemplo
spinbox = tk.Spinbox(janela, from_=0, to=10, width=5)
spinbox.pack(pady=10)

#capturar o valor do Spinbox
def mostrar_valor_spinbox():
    valor = spinbox.get()
    label.config(text=f"Valor do Spinbox: {valor}")

botao_spinbox = tk.Button(janela, text="Mostrar Valor do Spinbox", command=mostrar_valor_spinbox)
botao_spinbox.pack(pady=10)

janela.mainloop()