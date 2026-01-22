import tkinter as tk
from datetime import datetime

def atualizar_relogio():
    hora_atual = datetime.now()
    hora_atual_f = hora_atual.strftime('%H:%M:%S')
    label_relogio.set(hora_atual_f)
    janela.after(1000, atualizar_relogio)

janela = tk.Tk()
janela.title('Relógio Digital')
janela.geometry('200x75')
janela.resizable(False, False)
janela.configure(bg='#222222')
janela.option_add('*Font', 'DS-DIGITAL 36 bold')

label_relogio = tk.StringVar()
label = tk.Label(janela, textvariable=label_relogio, fg='#00ff00', bg='#222222')
label.pack(pady=10)

atualizar_relogio()

janela.mainloop()


