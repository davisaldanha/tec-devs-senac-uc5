import tkinter as tk

def on_double_click(event):
    # Recupera o widget que disparou o evento
    listbox = event.widget
    
    # Pega o índice do item clicado
    indice = listbox.curselection()
    
    if indice:  # Verifica se há algum item selecionado
        valor = listbox.get(indice[0])
        label.config(text=f"Você deu duplo clique em: {valor}")

# Janela principal
janela = tk.Tk()
janela.title("Listbox com duplo clique")
janela.geometry("300x250")

# Criando Listbox
listbox = tk.Listbox(janela)
listbox.pack(pady=10)

# Adicionando itens
for item in ["Python", "Java", "C++", "JavaScript", "Go", "Rust"]:
    listbox.insert(tk.END, item)

# Ligando o evento de duplo clique
listbox.bind("<Double-Button-1>", on_double_click)

# Label para mostrar resultado
label = tk.Label(janela, text="Dê um duplo clique em um item")
label.pack(pady=10)

janela.mainloop()