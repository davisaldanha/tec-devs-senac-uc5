'''Aula 07/01 - Quarta-Feira'''
import tkinter as tk

janela = tk.Tk()
janela.title('Minha Primeira Janela')
janela.geometry('400x300')

#impedir o redimensionamento
janela.resizable(False, False)

#ícone da janela
janela.iconbitmap('./assets/main-icon.ico')

#Cor do fundo
janela.configure(bg="#260404")

#Definir fonte padrão
janela.option_add('*Font', 'Arial 12')

#Layout - Rótulo
label = tk.Label(janela, text="Olá, Mundo!", fg='#ffffff', bg='#260404', font=('Helvetica', 24))
label.pack(pady=10)

#Layout - Botão
def clicar_botao():
    label.config(text='Botão cliquado!')

botao = tk.Button(janela, text='Clique aqui', command=clicar_botao)
botao.pack(pady=10)

#Layout - Entry
entrada = tk.Entry(janela)
entrada.pack(pady=10)

#Capturando o texto do campo de entrada ao pressionar Enter
def capturar_entrada(event):
    label.config(text=f'Você digitou: {entrada.get()}')

entrada.bind('<Return>', capturar_entrada)

#PhotoImage
imagem = tk.PhotoImage(file='./assets/login.png', format='png')
imagem = imagem.subsample(2)

label_image = tk.Label(janela, image=imagem, bg='#260404')
label_image.pack(pady=10)

janela.mainloop()