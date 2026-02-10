#Criar um cronometro simples com tkinter
import tkinter as tk
class Cronometro:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronômetro Simples")
        self.master.geometry("450x150")
        self.master.configure(bg="#333333")
        self.master.option_add("*Font", "Helvetica 24 bold")
        self.master.grab_set()
        self.master.attributes("-topmost", True)

        self.tempo = 0
        self.rodando = False

        self.texto_dinamico = tk.StringVar()
        self.texto_dinamico.set("00:00:00")

        self.label_cronometro = tk.Label(master, textvariable=self.texto_dinamico, fg="#FFFFFF", bg="#333333")
        self.label_cronometro.pack(pady=20)

        self.botao_iniciar = tk.Button(master, text="Iniciar", command=self.iniciar)
        self.botao_iniciar.pack(side=tk.LEFT, padx=10)

        self.botao_parar = tk.Button(master, text="Parar", command=self.parar)
        self.botao_parar.pack(side=tk.LEFT, padx=10)

        self.botao_resetar = tk.Button(master, text="Resetar", command=self.resetar)
        self.botao_resetar.pack(side=tk.LEFT, padx=10)

    def atualizar_cronometro(self):
        if self.rodando:
            self.tempo += 1
            horas = self.tempo // 3600
            minutos = (self.tempo % 3600) // 60
            segundos = self.tempo % 60
            self.texto_dinamico.set(f"{horas:02}:{minutos:02}:{segundos:02}")
            self.master.after(1000, self.atualizar_cronometro)

    def iniciar(self):
        if not self.rodando:
            self.rodando = True
            self.atualizar_cronometro()

    def parar(self):
        self.rodando = False

    def resetar(self):
        self.rodando = False
        self.tempo = 0
        self.texto_dinamico.set("00:00:00")

if __name__ == "__main__":
    janela = tk.Tk()
    cronometro = Cronometro(janela)
    janela.mainloop()