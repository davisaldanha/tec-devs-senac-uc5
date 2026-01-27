'''Botões customizados com CustomTkinter'''

import customtkinter as ctk

from app.gui.styles.styles import (
    BUTTON_BG,
    BUTTON_DANGER_BG,
    BUTTON_STYLE,
    FONT_BUTTON,
    BUTTON_HOVER,
    BUTTON_FG,
    BUTTON_DANGER_HOVER,
    BUTTON_CORNER_RADIUS,
    BUTTON_HEIGHT
)

class CustomButton(ctk.CTkButton):
    '''Botão customizado para ações normais'''
    def __init__(self, master, text='', command=None, **kwargs):
        super.__init__(
            master,
            text=text,
            command=command,
            fg_color=BUTTON_BG,
            text_color=BUTTON_FG,
            hover_color=BUTTON_HOVER,
            font=FONT_BUTTON,
            height=BUTTON_HEIGHT,
            corner_radius=BUTTON_CORNER_RADIUS,
            **kwargs,
        )

class DangerButton(ctk.CTkButton):
    '''Botão customizado para ações de risco (delete, etc)'''
    def __init__(self, master, text='', command=None, **kwargs):
        super.__init__(
            master,
            text=text,
            command=command,
            fg_color=BUTTON_DANGER_BG,
            text_color=BUTTON_FG,
            hover_color=BUTTON_DANGER_HOVER,
            font=FONT_BUTTON,
            height=BUTTON_HEIGHT,
            corner_radius=BUTTON_CORNER_RADIUS,
            **kwargs,
        )

class IconButton(ctk.CTkButton):
    '''Botão com ícone (apenas símbolo)'''
    def __init__(self, master, text='', width=40, command=None, **kwargs):
        super.__init__(
            master,
            text=text,
            command=command,
            fg_color=BUTTON_BG,
            text_color=BUTTON_FG,
            hover_color=BUTTON_HOVER,
            font=FONT_BUTTON,
            height=BUTTON_HEIGHT,
            corner_radius=BUTTON_CORNER_RADIUS,
            width= 40,
            **kwargs,
        )