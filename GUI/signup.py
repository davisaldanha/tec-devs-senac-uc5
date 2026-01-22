import tkinter as tk
from tkinter import messagebox

def salvar():
    nome = entry_nome.get()
    email = entry_email.get()
    genero = genero_var.get()
    interesses = []
    if chk_python_var.get():
        interesses.append("Python")
    if chk_java_var.get():
        interesses.append("Java")
    if chk_js_var.get():
        interesses.append("JavaScript")
    comentarios = txt_comentarios.get("1.0", tk.END).strip()
    cidade = listbox_cidades.get(tk.ACTIVE)

    resumo = f"""
    Nome: {nome}
    Email: {email}
    Gênero: {genero}
    Interesses: {', '.join(interesses)}
    Cidade: {cidade}
    Comentários: {comentarios}
    """
    messagebox.showinfo("Cadastro Salvo", resumo)

# Janela principal
root = tk.Tk()
root.title("Tela de Cadastro")

# Menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

menu_arquivo = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar)
menu_arquivo.add_separator()
menu_arquivo.add_command(label="Sair", command=root.quit)

# Frame principal
frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack()

# Nome
tk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1)

# Email
tk.Label(frame_form, text="Email:").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=1, column=1)

# Gênero (Radiobutton)
tk.Label(frame_form, text="Gênero:").grid(row=2, column=0, sticky="w")
genero_var = tk.StringVar(value="Não informado")
tk.Radiobutton(frame_form, text="Masculino", variable=genero_var, value="Masculino").grid(row=2, column=1, sticky="w")
tk.Radiobutton(frame_form, text="Feminino", variable=genero_var, value="Feminino").grid(row=2, column=2, sticky="w")

# Interesses (Checkbutton)
tk.Label(frame_form, text="Interesses:").grid(row=3, column=0, sticky="w")
chk_python_var = tk.BooleanVar()
chk_java_var = tk.BooleanVar()
chk_js_var = tk.BooleanVar()
tk.Checkbutton(frame_form, text="Python", variable=chk_python_var).grid(row=3, column=1, sticky="w")
tk.Checkbutton(frame_form, text="Java", variable=chk_java_var).grid(row=3, column=2, sticky="w")
tk.Checkbutton(frame_form, text="JavaScript", variable=chk_js_var).grid(row=3, column=3, sticky="w")

# Listbox (Cidades)
tk.Label(frame_form, text="Cidade:").grid(row=4, column=0, sticky="w")
listbox_cidades = tk.Listbox(frame_form, height=5)
cidades = ["Fortaleza", "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
for cidade in cidades:
    listbox_cidades.insert(tk.END, cidade)
listbox_cidades.grid(row=4, column=1, columnspan=2, sticky="w")

# Text (Comentários)
tk.Label(frame_form, text="Comentários:").grid(row=5, column=0, sticky="nw")
txt_comentarios = tk.Text(frame_form, width=40, height=5)
txt_comentarios.grid(row=5, column=1, columnspan=3)

# Botão salvar
btn_salvar = tk.Button(root, text="Salvar Cadastro", command=salvar)
btn_salvar.pack(pady=10)

root.mainloop()