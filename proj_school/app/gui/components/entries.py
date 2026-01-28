import customtkinter as ctk

from app.gui.styles.fonts import *
from app.gui.styles.colors import *
from app.gui.styles.styles import *

class CustomEntry(ctk.CTkEntry):
    '''Campo de entrada customizado'''
    def  __init__(self, master, placeholder='', **kwargs):
        super().__init__(
            master,
            fg_color=ENTRY_BG,
            text_color=ENTRY_FG,
            border_color=ENTRY_BORDER,
            font=FONT_ENTRY,
            height=ENTRY_HEIGHT,
            corner_radius=ENTRY_CORNER_RADIUS,
            border_width=2,
            **kwargs,
        )
        self.placeholder = placeholder
        self.is_placeholder = False

        if placeholder:
            pass
    
    def _set_placeholder(self):
        '''Definir o placeholder visível'''
        self.insert(0, self.placeholder)
        self.configure(text_color=TEXT_MUDED)
        self.is_placeholder = True
    
    def _on_focus_in(self, event):
        '''Evento quando o campo recebe foco'''
        if self.is_placeholder:
            self.delete(0, ctk.END)
            self.configure(text_color=ENTRY_FG)
            self.is_placeholder = False
    
    def _on_focus_out(self, event):
        '''Evento quando o campo perde foco'''
        if self.get() == '':
            self._set_placeholder()
    
    def get_value(self):
        '''Retornar o valor sem o placeholder'''
        if self.is_placeholder:
            return ''
        return self.get()

class CustomTextBox(ctk.CTkTextbox):
    '''Caixa de entrada customizada'''
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color=ENTRY_BG,
            text_color=ENTRY_FG,
            border_color=ENTRY_BORDER,
            font=FONT_ENTRY,
            corner_radius=ENTRY_CORNER_RADIUS,
            border_width=2,
            **kwargs,
        )

class CustomComboBox(ctk.CTkComboBox):
    '''ComboBox customizado'''
    def __init__(self, master, values=None ,**kwargs):
        super().__init__(
            master,
            values=values or [],
            fg_color=ENTRY_BG,
            text_color=ENTRY_FG,
            border_color=ENTRY_BORDER,
            font=FONT_ENTRY,
            corner_radius=ENTRY_CORNER_RADIUS,
            border_width=2,
            height=ENTRY_HEIGHT
            **kwargs,
        )