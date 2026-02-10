import tkinter as tk

janela = tk.Tk()
janela.title("Minha Primeira GUI")
janela.geometry("400x300")

#Configurações básicas da janela
'''
- Título
- Tamanho
- Redimensionamento
- Ícone
- Cor de fundo
- Fonte padrão
- Layout
'''
# Redimensionamento
#janela.resizable(width=False, height=False) # Impede redimensionamento

#Ícone da janela
janela.iconbitmap('computadores.ico')

# Cor de fundo
janela.configure(bg="#75701b")

# Fonte padrão
janela.option_add("*Font", "Helvetica 12")

# Layout - Adicionando um rótulo
label = tk.Label(janela, text="Olá, Mundo!", font=("Arial", 16), bg="#75701b")
label.pack(pady=20) # Adiciona um rótulo com texto

# Adicionando um botão
def clicar_botao():
    label.config(text="Botão clicado!")

botao = tk.Button(janela, text="Clique aqui", command=clicar_botao)
botao.pack(pady=10)

# Adicionando um campo de entrada
entrada = tk.Entry(janela)
entrada.pack(pady=10)

#Capturando o texto do campo de entrada ao pressionar Enter
def capturar_entrada(event):
    texto = entrada.get()
    label.config(text=f"Você digitou: {texto}")

entrada.bind("<Return>", capturar_entrada)

#Adicionando imagem no label
imagem = tk.PhotoImage(file="image.png", format="png")

#definir tamanho da imagem
imagem = imagem.subsample(4, 4)  # Reduz a imagem para 1/4 do tamanho original
label_imagem = tk.Label(janela, image=imagem)
label_imagem.pack(pady=10)

#Variável para o texto
texto_dinamico = tk.StringVar()

entrada_dinamica = tk.Entry(janela, textvariable=texto_dinamico)
entrada_dinamica.pack(pady=10)

print(texto_dinamico.get())

# Widget de texto
texto_widget = tk.Text(janela, height=5, width=30)
texto_widget.pack(pady=10)

#Capturar o conteúdo do widget de texto
def capturar_texto_widget():
    conteudo = texto_widget.get("1.0", tk.END)  # Pega todo o conteúdo do widget
    label.config(text=f"Conteúdo do Text:\n{conteudo}")

botao_texto = tk.Button(janela, text="Capturar Texto", command=capturar_texto_widget)
botao_texto.pack(pady=10)

# Exemplo de grid layout
#label1 = tk.Label(janela, text="Label 1", bg="#75701b")
#label2 = tk.Label(janela, text="Label 2", bg="#75701b")
#label1.grid(row=0, column=0, padx=10, pady=10)
#label2.grid(row=0, column=1, padx=10, pady=10)

# Inicia o loop principal da janela
janela.mainloop()


