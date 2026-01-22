import tkinter as tk
from tkinter import messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Tela de Login')
        self.root.geometry('300x200')
        self.root.configure(bg='#222222')
        self.root.option_add('*Font', ('Cascadia Code', 16))

        #Imagem com PhotoImage
        self.image = tk.PhotoImage(file='login.png', format='png')
        self.image = self.image.subsample(2)
        self.label_image = tk.Label(root, image=self.image, bg='#222222')
        self.label_image.grid(row=0, column=0, columnspan=2, pady=5, padx=5)

        #Campos de Entrada
        self.label_email = tk.Label(root, text='E-mail', fg='#ffffff', bg='#222222')
        self.label_email.grid(row=1, column=0, pady=5, padx=5)

        self.input_email = tk.Entry(root)
        self.input_email.grid(row=1, column=1, pady=5, padx=5)

        self.label_password = tk.Label(root, text='Senha', fg='#ffffff', bg='#222222')
        self.label_password.grid(row=2, column=0, pady=5, padx=5)

        self.input_password = tk.Entry(root, show='*')
        self.input_password.grid(row=2, column=1, pady=5, padx=5)

        #Botão
        self.button_login = tk.Button(root, text="Entrar", command=self.valid_login)
        self.button_login.grid(row=3, column=0, columnspan=2, pady=10)

    def valid_login(self):
        user = self.input_email.get()
        password = self.input_password.get()

        if user == 'admin' and password == '123':
            messagebox.showinfo('Login Bem-Sucedido', f"Bem Vindo, {user}")
        else:
            messagebox.showerror('Erro de login!', 'E-mail ou senha incorretos!')



if __name__ == '__main__':
    window = tk.Tk()
    app = LoginApp(window)
    window.mainloop()