import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de Frame")
janela.geometry("400x300")

#Label
label = tk.Label(janela, text="Segunda-Feira", font=('DS-DIGITAL', 24), bg="#75701b")
label.pack(pady=20)

#Frame 
frame = tk.Frame(janela, bg="#333333", padx=10, pady=10)
frame.pack(pady=20)

label_frame = tk.Label(frame, text="Dentro do frame", bg="#333333", fg="#FFFFFF")
label_frame.grid(row=0, column=0)

botao_frame = tk.Button(frame, text="Botão do Frame")
botao_frame.grid(row=1, column=0, pady=10)

var_check = tk.IntVar()
checkbutton = tk.Checkbutton(janela, text="Opção", variable=var_check, bg="#75701b")
checkbutton.pack(pady=10)

def verificar_checkbutton():
    estado = var_check.get()
    label.config(text=f"Checkbutton está: {'Selecionado' if estado else 'Não Selecionado'}")

botao_check = tk.Button(janela, text="Verificar Checkbutton", command=verificar_checkbutton)
botao_check.pack(pady=10)

frame2 = tk.Frame(janela, bg="#555555", padx=10, pady=10)
frame2.pack(pady=20)

label_frame2 = tk.Label(frame2, text="Segundo Frame", bg="#555555", fg="#FFFFFF")
label_frame2.grid(row=0, column=0)

#Radiobuttons dentro frame2
var_radio = tk.StringVar(value="Opção 1")
radio1 = tk.Radiobutton(frame2, text="Opção 1", variable=var_radio, value="Opção 1", bg="#555555")
radio2 = tk.Radiobutton(frame2, text="Opção 2", variable=var_radio, value="Opção 2", bg="#555555")
radio1.grid(row=1, column=0, sticky='w')
radio2.grid(row=2, column=0, sticky='w')

def mostrar_opcao_radio():
    label.config(text=f"Selecionado: {var_radio.get()}")

botao_radio = tk.Button(janela, text="Mostrar Opção Selecionada", command=mostrar_opcao_radio)
botao_radio.pack(pady=10)

#-----------------------------------------------------------------------------------
