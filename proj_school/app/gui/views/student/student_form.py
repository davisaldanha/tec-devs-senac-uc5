"""
Formulário de Alunos (Criar/Editar)
"""

import customtkinter as ctk
from app.gui.styles import (
    PADDING_MD,
    PADDING_LG,
    FONT_SUBTITLE,
    LABEL_FG,
    FRAME_BG,
    TEXT_SECONDARY,
)
from app.gui.components.frames import CustomFrame, SectionFrame
from app.gui.components.buttons import CustomButton, DangerButton
from app.gui.components.entries import CustomEntry
from app.gui.controllers.student_controller import StudentController


class StudentFormView(ctk.CTkFrame):
    """View para criar/editar alunos"""

    def __init__(self, parent, student_id=None, on_save_callback=None, on_cancel_callback=None, **kwargs):
        super().__init__(parent, fg_color=FRAME_BG, **kwargs)

        self.student_id = student_id
        self.on_save_callback = on_save_callback
        self.on_cancel_callback = on_cancel_callback

        # Título
        title_text = "Novo Aluno" if student_id is None else "Editar Aluno"
        title_label = ctk.CTkLabel(
            self,
            text=title_text,
            text_color=LABEL_FG,
            font=FONT_SUBTITLE,
        )
        title_label.pack(padx=PADDING_LG, pady=PADDING_LG, anchor="w")

        # Frame de conteúdo
        content_frame = CustomFrame(self)
        content_frame.pack(fill="both", expand=True, padx=PADDING_LG, pady=PADDING_MD)

        # Seção de dados pessoais
        personal_section = SectionFrame(content_frame, title="Dados Pessoais")
        personal_section.pack(fill="x", padx=PADDING_MD, pady=PADDING_MD)

        personal_content = personal_section.get_content_frame()

        # Nome
        ctk.CTkLabel(personal_content, text="Nome", text_color=LABEL_FG).pack(anchor="w", pady=(0, 5))
        self.nome_entry = CustomEntry(personal_content, placeholder="Digite o nome")
        self.nome_entry.pack(fill="x", pady=(0, PADDING_MD))

        # Sobrenome
        ctk.CTkLabel(personal_content, text="Sobrenome", text_color=LABEL_FG).pack(anchor="w", pady=(0, 5))
        self.sobrenome_entry = CustomEntry(personal_content, placeholder="Digite o sobrenome")
        self.sobrenome_entry.pack(fill="x", pady=(0, PADDING_MD))

        # Seção de contato
        contact_section = SectionFrame(content_frame, title="Contato")
        contact_section.pack(fill="x", padx=PADDING_MD, pady=PADDING_MD)

        contact_content = contact_section.get_content_frame()

        # Telefone
        ctk.CTkLabel(contact_content, text="Telefone (11 dígitos)", text_color=LABEL_FG).pack(anchor="w", pady=(0, 5))
        self.telefone_entry = CustomEntry(contact_content, placeholder="11999999999")
        self.telefone_entry.pack(fill="x", pady=(0, PADDING_MD))

        # CPF
        ctk.CTkLabel(contact_content, text="CPF (11 dígitos)", text_color=LABEL_FG).pack(anchor="w", pady=(0, 5))
        self.cpf_entry = CustomEntry(contact_content, placeholder="12345678901")
        self.cpf_entry.pack(fill="x", pady=(0, PADDING_MD))

        # Seção de informações
        info_section = SectionFrame(content_frame, title="Informações")
        info_section.pack(fill="x", padx=PADDING_MD, pady=PADDING_MD)

        info_content = info_section.get_content_frame()

        # Idade
        ctk.CTkLabel(info_content, text="Idade", text_color=LABEL_FG).pack(anchor="w", pady=(0, 5))
        self.idade_entry = CustomEntry(info_content, placeholder="Ex: 18")
        self.idade_entry.pack(fill="x", pady=(0, PADDING_MD))

        # Data de Nascimento
        ctk.CTkLabel(info_content, text="Data de Nascimento (DD/MM/YYYY)", text_color=LABEL_FG).pack(anchor="w", pady=(0, 5))
        self.data_nasc_entry = CustomEntry(info_content, placeholder="01/01/2006")
        self.data_nasc_entry.pack(fill="x", pady=(0, PADDING_MD))

        # Frame de botões
        button_frame = CustomFrame(self)
        button_frame.pack(fill="x", padx=PADDING_LG, pady=PADDING_LG)

        save_button = CustomButton(button_frame, text="Salvar", command=self._on_save)
        save_button.pack(side="left", padx=(0, PADDING_MD), fill="both", expand=True)

        cancel_button = DangerButton(button_frame, text="Cancelar", command=self._on_cancel)
        cancel_button.pack(side="left", fill="both", expand=True)

        # Carregar dados se editar
        if student_id:
            self._load_student_data()

    def _load_student_data(self):
        """Carrega dados do aluno"""
        student = StudentController.get_student_by_id(self.student_id)
        if student:
            self.nome_entry.delete(0, "end")
            self.nome_entry.insert(0, student[1] or "")
            self.sobrenome_entry.delete(0, "end")
            self.sobrenome_entry.insert(0, student[2] or "")
            self.idade_entry.delete(0, "end")
            self.idade_entry.insert(0, str(student[3]) or "")
            self.telefone_entry.delete(0, "end")
            self.telefone_entry.insert(0, student[4] or "")
            self.cpf_entry.delete(0, "end")
            self.cpf_entry.insert(0, student[5] or "")
            self.data_nasc_entry.delete(0, "end")
            self.data_nasc_entry.insert(0, student[6] or "")

    def _on_save(self):
        """Salva o aluno"""
        try:
            nome = self.nome_entry.get_value()
            sobrenome = self.sobrenome_entry.get_value()
            idade = int(self.idade_entry.get_value())
            telefone = self.telefone_entry.get_value()
            cpf = self.cpf_entry.get_value()
            data_nasc = self.data_nasc_entry.get_value()

            if self.student_id:
                # Editar
                success = StudentController.update_student(
                    self.student_id, nome, sobrenome, idade, telefone, cpf, data_nasc
                )
            else:
                # Criar
                success = StudentController.create_student(
                    nome, sobrenome, idade, telefone, cpf, data_nasc
                )

            if success and self.on_save_callback:
                self.on_save_callback()

        except ValueError:
            print("Erro: idade deve ser um número")

    def _on_cancel(self):
        """Cancela a edição"""
        if self.on_cancel_callback:
            self.on_cancel_callback()
