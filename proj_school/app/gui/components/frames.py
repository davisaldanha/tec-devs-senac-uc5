import customtkinter as ctk

from app.gui.styles.fonts import *
from app.gui.styles.colors import *
from app.gui.styles.styles import *

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
    
    def get_content_frame(self):
        '''Retorna o frame de conteúdo para adicionar widgets'''
        return self.content_frame

class CustomFrame(ctk.CTkFrame):
    '''Frame customizado com padding padrão'''
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color='white',
            corner_radius=FRAME_CORNER_RADIUS,
            border_width=1,
            border_color=FRAME_BG,
            **kwargs,
        )


    