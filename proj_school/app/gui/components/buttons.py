"""
Botões customizados com CustomTkinter
"""

import customtkinter as ctk
from app.gui.styles import (
    BUTTON_STYLE,
    BUTTON_DANGER_STYLE,
    FONT_BUTTON,
    BUTTON_BG,
    BUTTON_HOVER,
    BUTTON_DANGER_BG,
    BUTTON_DANGER_HOVER,
    BUTTON_FG,
)


class CustomButton(ctk.CTkButton):
    """Botão customizado para ações normais"""

    def __init__(self, master, text="", command=None, **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color=BUTTON_BG,
            text_color=BUTTON_FG,
            hover_color=BUTTON_HOVER,
            font=FONT_BUTTON,
            height=40,
            corner_radius=8,
            **kwargs,
        )


class DangerButton(ctk.CTkButton):
    """Botão customizado para ações de risco (delete, etc)"""

    def __init__(self, master, text="", command=None, **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            fg_color=BUTTON_DANGER_BG,
            text_color=BUTTON_FG,
            hover_color=BUTTON_DANGER_HOVER,
            font=FONT_BUTTON,
            height=40,
            corner_radius=8,
            **kwargs,
        )


class IconButton(ctk.CTkButton):
    """Botão com ícone (apenas símbolo)"""

    def __init__(self, master, text="", command=None, width=40, **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            width=width,
            height=40,
            fg_color=BUTTON_BG,
            text_color=BUTTON_FG,
            hover_color=BUTTON_HOVER,
            corner_radius=8,
            **kwargs,
        )
