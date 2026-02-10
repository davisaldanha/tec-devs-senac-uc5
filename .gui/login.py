#tela de login 
import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tela de Login")
        self.master.geometry("300x200")
        self.master.configure(bg="#444444")
        self.master.option_add("*Font", "Helvetica 12")

        self.image = tk.PhotoImage(file="login.png", format="png")
        self.image = self.image.subsample(3, 3)
        self.label_imagem = tk.Label(master, image=self.image, bg="#444444")
        self.label_imagem.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

        self.label_usuario = tk.Label(master, text="Usuário:", fg="#FFFFFF", bg="#444444")
        self.label_usuario.grid(row=1, column=0, pady=5, padx=5)

        self.entrada_usuario = tk.Entry(master)
        self.entrada_usuario.grid(row=1, column=1, pady=5, padx=5)

        self.label_senha = tk.Label(master, text="Senha:", fg="#FFFFFF", bg="#444444")
        self.label_senha.grid(row=2, column=0, pady=5, padx=5)

        self.entrada_senha = tk.Entry(master, show="*")
        self.entrada_senha.grid(row=2, column=1, pady=5, padx=5)

        self.botao_login = tk.Button(master, text="Login", command=self.verificar_login)
        self.botao_login.grid(row=3, column=0, columnspan=2, pady=10)

    def verificar_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()
        if usuario == "admin" and senha == "senha123":
            messagebox.showinfo("Login Bem-Sucedido", "Bem-vindo, admin!")
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos.")

if __name__ == "__main__":
    janela = tk.Tk()
    app = LoginApp(janela)
    janela.mainloop()