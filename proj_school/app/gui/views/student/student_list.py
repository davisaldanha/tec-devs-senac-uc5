"""
Lista de Alunos
"""

import customtkinter as ctk
from app.gui.styles import (
    PADDING_MD,
    PADDING_LG,
    FONT_SUBTITLE,
    LABEL_FG,
    FRAME_BG,
)
from app.gui.components.frames import CustomFrame
from app.gui.components.buttons import CustomButton
from app.gui.components.entries import CustomEntry
from app.gui.components.tables import CustomTable
from app.gui.controllers.student_controller import StudentController


class StudentListView(ctk.CTkFrame):
    """View para listar alunos"""

    def __init__(self, parent, on_edit_callback=None, on_delete_callback=None, **kwargs):
        super().__init__(parent, fg_color=FRAME_BG, **kwargs)

        self.on_edit_callback = on_edit_callback
        self.on_delete_callback = on_delete_callback

        # Título
        title_label = ctk.CTkLabel(
            self,
            text="Lista de Alunos",
            text_color=LABEL_FG,
            font=FONT_SUBTITLE,
        )
        title_label.pack(padx=PADDING_LG, pady=PADDING_LG, anchor="w")

        # Frame de controles
        control_frame = CustomFrame(self)
        control_frame.pack(fill="x", padx=PADDING_LG, pady=PADDING_MD)

        # Busca
        search_entry = CustomEntry(control_frame, placeholder="Buscar aluno...", width=200)
        search_entry.pack(side="left", padx=(0, PADDING_MD), fill="x", expand=True)

        # Botões
        add_button = CustomButton(control_frame, text="+ Novo", command=self._on_new_click)
        add_button.pack(side="left", padx=(0, PADDING_MD))

        edit_button = CustomButton(control_frame, text="✎ Editar", command=self._on_edit_click)
        edit_button.pack(side="left", padx=(0, PADDING_MD))

        delete_button = CustomButton(control_frame, text="🗑 Deletar", command=self._on_delete_click)
        delete_button.pack(side="left")

        # Tabela
        self.table = CustomTable(
            self,
            columns=["ID", "Nome", "Sobrenome", "Idade", "Telefone", "CPF"],
            height=400,
        )
        self.table.pack(fill="both", expand=True, padx=PADDING_LG, pady=PADDING_MD)

        # Carregar dados
        self._load_students()

    def _load_students(self):
        """Carrega alunos na tabela"""
        self.table.clear()
        students = StudentController.get_all_students()
        for student in students:
            if student:
                self.table.insert_row(student)

    def _on_new_click(self):
        """Callback para novo aluno"""
        if self.on_edit_callback:
            self.on_edit_callback(None)

    def _on_edit_click(self):
        """Callback para editar aluno"""
        row = self.table.get_selected_row()
        if row and self.on_edit_callback:
            self.on_edit_callback(row[0])  # Passa o ID

    def _on_delete_click(self):
        """Callback para deletar aluno"""
        row = self.table.get_selected_row()
        if row and self.on_delete_callback:
            self.on_delete_callback(row[0])  # Passa o ID

    def refresh(self):
        """Recarrega a lista"""
        self._load_students()
