'''Form CRUD alunos'''

from ...components.frames import MyFrame
import customtkinter as ctk

class StudentFormView(MyFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.label = ctk.CTkLabel(self, text="Formulário Estudante")
        self.label.pack(padx=20, pady=10)

        self.frame = ctk.CTkFrame(self, corner_radius=10)
        self.frame.pack(padx=20, pady=10)

        self.label_name = ctk.CTkLabel(self.frame, text="Nome").grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = ctk.CTkEntry(self.frame, placeholder_text="Nome do aluno")

        



