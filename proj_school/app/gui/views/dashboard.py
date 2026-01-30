import customtkinter as ctk

from app.gui.styles.fonts import *
from app.gui.styles.colors import *
from app.gui.styles.styles import *

from app.gui.components.frames import CardFrame

class DashboardView(ctk.CTkFrame):
    '''View Dashboard'''

    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=FRAME_BG, **kwargs)

        #Título
        title_label = ctk.CTkLabel(
            self,
            text='Dashboard',
            text_color=LABEL_FG,
            font=FONT_TITLE
        )
        title_label.pack(padx=PADDING_LG, pady=PADDING_LG, anchor='w')

        #Subtítulo
        subtitle_label = ctk.CTkLabel(
            self,
            text='Bem-vindo ao Sistema de Gerenciamento Escolar',
            text_color=LABEL_FG,
            font=FONT_SUBTITLE
        )
        title_label.pack(padx=PADDING_LG, pady=(0, PADDING_LG), anchor='w')