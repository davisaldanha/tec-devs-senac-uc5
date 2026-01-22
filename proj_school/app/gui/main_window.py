"""
Janela Principal da Aplicação
"""

import customtkinter as ctk
from app.gui.styles import (
    PRIMARY_COLOR,
    BG_PRIMARY,
    SIDEBAR_WIDTH,
    MIN_WINDOW_WIDTH,
    MIN_WINDOW_HEIGHT,
)
from app.gui.views.dashboard import DashboardView
from app.gui.views.student.student_list import StudentListView
from app.gui.views.student.student_form import StudentFormView
from app.gui.components.dialogs import MessageDialog, ConfirmDialog
from app.gui.controllers.student_controller import StudentController


class MainWindow(ctk.CTk):
    """Janela principal da aplicação"""

    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Sistema de Gerenciamento Escolar")
        self.geometry(f"{MIN_WINDOW_WIDTH}x{MIN_WINDOW_HEIGHT}")
        self.minsize(MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configurar grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Sidebar
        self._create_sidebar()

        # Frame principal
        self.main_frame = ctk.CTkFrame(self, fg_color=BG_PRIMARY)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Stack de views
        self.views = {}
        self.current_view = None

        # Carregar views
        self._load_views()

        # Mostrar dashboard
        self.show_view("dashboard")

    def _create_sidebar(self):
        """Cria a barra lateral de navegação"""
        sidebar = ctk.CTkFrame(self, fg_color=PRIMARY_COLOR, width=SIDEBAR_WIDTH)
        sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        sidebar.grid_rowconfigure(6, weight=1)

        # Logo/Título
        title_label = ctk.CTkLabel(
            sidebar,
            text="Escola",
            text_color="white",
            font=("Segoe UI", 24, "bold"),
        )
        title_label.pack(padx=20, pady=20)

        # Separator
        separator = ctk.CTkFrame(sidebar, height=2, fg_color="white")
        separator.pack(fill="x", padx=20, pady=10)

        # Menu items
        menu_items = [
            ("🏠 Dashboard", "dashboard"),
            ("👥 Alunos", "students"),
            ("👨‍🏫 Professores", "professors"),
            ("📚 Cursos", "courses"),
            ("🎓 Turmas", "classes"),
        ]

        for label, view_id in menu_items:
            btn = ctk.CTkButton(
                sidebar,
                text=label,
                text_color="white",
                fg_color="transparent",
                hover_color="rgba(255, 255, 255, 0.1)",
                command=lambda v=view_id: self.show_view(v),
                font=("Segoe UI", 12),
                height=40,
                anchor="w"
            )
            btn.pack(fill="x", padx=10, pady=5)

        # Separator
        separator2 = ctk.CTkFrame(sidebar, height=2, fg_color="white")
        separator2.pack(fill="x", padx=20, pady=10, side="bottom")

        # Exit button
        exit_btn = ctk.CTkButton(
            sidebar,
            text="❌ Sair",
            text_color="white",
            fg_color="transparent",
            hover_color="rgba(255, 0, 0, 0.2)",
            command=self.quit,
            font=("Segoe UI", 12),
            height=40,
            anchor="w"
        )
        exit_btn.pack(fill="x", padx=10, pady=5, side="bottom")

    def _load_views(self):
        """Carrega todas as views"""
        self.views["dashboard"] = DashboardView(self.main_frame)

        self.views["students"] = StudentListView(
            self.main_frame,
            on_edit_callback=self._on_edit_student,
            on_delete_callback=self._on_delete_student,
        )

    def show_view(self, view_id):
        """Mostra uma view específica"""
        if self.current_view:
            self.current_view.grid_forget()

        if view_id not in self.views:
            print(f"View {view_id} não encontrada")
            return

        self.current_view = self.views[view_id]
        self.current_view.grid(row=0, column=0, sticky="nsew")

    def _on_edit_student(self, student_id):
        """Callback para editar aluno"""
        # Criar/mostrar view de formulário
        form_view = StudentFormView(
            self.main_frame,
            student_id=student_id,
            on_save_callback=self._on_student_saved,
            on_cancel_callback=self._on_student_cancelled,
        )
        self.current_view.grid_forget()
        self.current_view = form_view
        self.current_view.grid(row=0, column=0, sticky="nsew")

    def _on_student_saved(self):
        """Callback após salvar aluno"""
        MessageDialog(self, "Sucesso", "Aluno salvo com sucesso!")
        self.show_view("students")
        self.views["students"].refresh()

    def _on_student_cancelled(self):
        """Callback após cancelar edição"""
        self.show_view("students")

    def _on_delete_student(self, student_id):
        """Callback para deletar aluno"""
        dialog = ConfirmDialog(
            self, "Confirmar Exclusão", f"Tem certeza que deseja deletar este aluno?"
        )
        self.wait_window(dialog)

        if dialog.result:
            if StudentController.delete_student(student_id):
                MessageDialog(self, "Sucesso", "Aluno deletado com sucesso!")
                self.views["students"].refresh()
            else:
                MessageDialog(self, "Erro", "Erro ao deletar aluno")


def main():
    """Função principal"""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
