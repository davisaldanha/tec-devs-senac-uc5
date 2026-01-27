import customtkinter as ctk

from app.gui.styles.fonts import *

class CardFrame(ctk.CTkFrame):
    '''Frame customizado para exibir cards informativos'''
    def __init__(self, master, title='', **kwargs):
        super.__init__(
            master,
            fg_color='white',
            corner_radius=10,
            border_width=1,
            border_color='#E0E0E0',
            **kwargs,
        )
    
        # Título do card
        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=FONT_TITLE,
            text_color='#333333'
        )
        title_label.pack(padx=15, pady=(15, 10), anchor="w")

        # Frame de conteúdo
        self.content_frame = ctk.CtkFrame(self, fg_color='trasparent')
        self.content_frame.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        