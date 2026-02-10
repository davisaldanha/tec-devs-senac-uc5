import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Exemplo de Listbox")
janela.geometry("300x250")

# Criando um Listbox
listbox = tk.Listbox(janela, selectmode=tk.SINGLE)  
# selectmode pode ser:
# tk.SINGLE -> apenas um item
# tk.MULTIPLE -> múltiplos itens
# tk.BROWSE -> parecido com SINGLE, mas permite arrastar
# tk.EXTENDED -> múltiplos itens com Shift ou Ctrl

# Adicionando itens ao Listbox
itens = ["Python", "Java", "C++", "JavaScript", "Go", "Rust"]
for item in itens:
    listbox.insert(tk.END, item)

listbox.pack(pady=10)

# Função para mostrar o item selecionado
def mostrar_selecao():
    selecionado = listbox.get(tk.ACTIVE)  # pega o item ativo
    label.config(text=f"Você selecionou: {selecionado}")

# Botão para confirmar seleção
botao = tk.Button(janela, text="Mostrar Seleção", command=mostrar_selecao)
botao.pack(pady=5)

# Label para exibir resultado
label = tk.Label(janela, text="Selecione um item da lista")
label.pack(pady=10)

# Inicia o loop da aplicação
janela.mainloop()