#fazendo um relógio com datetime e after tkinter
from datetime import datetime
import tkinter as tk

def atualizar_relogio():
    agora = datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    texto_dinamico.set(hora_formatada)
    janela.after(1000, atualizar_relogio)

# Configuração da janela
janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("300x150")
janela.configure(bg="#222222")
janela.option_add("*Font", "Helvetica 24 bold")
texto_dinamico = tk.StringVar()
label_relogio = tk.Label(janela, textvariable=texto_dinamico, fg="#00FF00", bg="#222222")
label_relogio.pack(pady=20)
atualizar_relogio()
janela.mainloop()

