"""
Dashboard/Home - Tela inicial da aplicação
"""

import customtkinter as ctk
from app.gui.styles import (
    PADDING_LG,
    FONT_TITLE,
    FONT_SUBTITLE,
    LABEL_FG,
    FRAME_BG,
)
from app.gui.components.frames import CardFrame


class DashboardView(ctk.CTkFrame):
    """View do Dashboard"""

    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=FRAME_BG, **kwargs)

        # Título
        title_label = ctk.CTkLabel(
            self,
            text="Dashboard",
            text_color=LABEL_FG,
            font=FONT_TITLE,
        )
        title_label.pack(padx=PADDING_LG, pady=PADDING_LG, anchor="w")

        # Subtítulo
        subtitle_label = ctk.CTkLabel(
            self,
            text="Bem-vindo ao Sistema de Gerenciamento Escolar",
            text_color=LABEL_FG,
            font=FONT_SUBTITLE,
        )
        subtitle_label.pack(padx=PADDING_LG, pady=(0, PADDING_LG), anchor="w")

        # Frame de cards
        cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        cards_frame.pack(fill="both", expand=True, padx=PADDING_LG, pady=PADDING_LG)

        # Cards informativos
        self._create_info_card(cards_frame, "👥 Alunos", "Gerenciar alunos")
        self._create_info_card(cards_frame, "👨‍🏫 Professores", "Gerenciar professores")
        self._create_info_card(cards_frame, "📚 Cursos", "Gerenciar cursos")
        self._create_info_card(cards_frame, "🎓 Turmas", "Gerenciar turmas")

    def _create_info_card(self, parent, title, description):
        """Cria um card informativo"""
        card = CardFrame(parent, title=title)
        card.pack(side="left", fill="both", expand=True, padx=PADDING_LG, pady=PADDING_LG)

        desc_label = ctk.CTkLabel(
            card.get_content_frame(),
            text=description,
            text_color=LABEL_FG,
            font=("Segoe UI", 12),
            wraplength=200,
        )
        desc_label.pack(padx=PADDING_LG, pady=PADDING_LG, fill="both", expand=True)
