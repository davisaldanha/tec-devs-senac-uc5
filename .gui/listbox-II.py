import tkinter as tk

def on_select(event):
    # Recupera o widget que disparou o evento
    listbox = event.widget
    
    # Pega os índices selecionados
    indices = listbox.curselection()
    
    # Pega os valores correspondentes
    valores = [listbox.get(i) for i in indices]
    
    # Atualiza o label com os itens escolhidos
    label.config(text=f"Selecionado: {', '.join(valores)}")

# Janela principal
janela = tk.Tk()
janela.title("Listbox com bind")
janela.geometry("300x250")

# Criando Listbox com múltipla seleção
listbox = tk.Listbox(janela, selectmode=tk.MULTIPLE)
listbox.pack(pady=10)

# Adicionando itens
for item in ["Python", "Java", "C++", "JavaScript", "Go", "Rust"]:
    listbox.insert(tk.END, item)

# Ligando o evento <<ListboxSelect>> à função on_select
listbox.bind("<<ListboxSelect>>", on_select)

# Label para mostrar resultado
label = tk.Label(janela, text="Selecione um item")
label.pack(pady=10)

janela.mainloop()