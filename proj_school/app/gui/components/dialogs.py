"""
Caixas de diálogo customizadas
"""

import customtkinter as ctk
from app.gui.components.buttons import CustomButton, DangerButton
from app.gui.styles import PADDING_MD, FONT_LABEL, LABEL_FG, FRAME_BG


class MessageDialog(ctk.CTkToplevel):
    """Diálogo para exibir mensagens"""

    def __init__(self, parent, title="Mensagem", message="", dialog_type="info"):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.result = None

        # Frame principal
        main_frame = ctk.CTkFrame(self, fg_color=FRAME_BG)
        main_frame.pack(fill="both", expand=True, padx=PADDING_MD, pady=PADDING_MD)

        # Mensagem
        message_label = ctk.CTkLabel(
            main_frame,
            text=message,
            text_color=LABEL_FG,
            font=FONT_LABEL,
            wraplength=350,
            justify="center",
        )
        message_label.pack(fill="both", expand=True, padx=PADDING_MD, pady=PADDING_MD)

        # Botão OK
        ok_button = CustomButton(main_frame, text="OK", command=self.ok_action)
        ok_button.pack(padx=PADDING_MD, pady=PADDING_MD, fill="x")

        self.center_window(parent)

    def ok_action(self):
        """Ação do botão OK"""
        self.result = True
        self.destroy()

    def center_window(self, parent):
        """Centraliza a janela em relação ao parent"""
        self.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() - self.winfo_width()) // 2
        y = parent.winfo_y() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")


class ConfirmDialog(ctk.CTkToplevel):
    """Diálogo para confirmação"""

    def __init__(self, parent, title="Confirmação", message=""):
        super().__init__(parent)
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.result = None

        # Frame principal
        main_frame = ctk.CTkFrame(self, fg_color=FRAME_BG)
        main_frame.pack(fill="both", expand=True, padx=PADDING_MD, pady=PADDING_MD)

        # Mensagem
        message_label = ctk.CTkLabel(
            main_frame,
            text=message,
            text_color=LABEL_FG,
            font=FONT_LABEL,
            wraplength=350,
            justify="center",
        )
        message_label.pack(fill="both", expand=True, padx=PADDING_MD, pady=PADDING_MD)

        # Frame de botões
        button_frame = ctk.CTkFrame(main_frame, fg_color=FRAME_BG)
        button_frame.pack(fill="x", padx=PADDING_MD, pady=PADDING_MD)

        # Botões
        yes_button = CustomButton(button_frame, text="Sim", command=self.yes_action)
        yes_button.pack(side="left", padx=(0, PADDING_MD), fill="both", expand=True)

        no_button = DangerButton(button_frame, text="Não", command=self.no_action)
        no_button.pack(side="left", fill="both", expand=True)

        self.center_window(parent)

    def yes_action(self):
        """Ação do botão Sim"""
        self.result = True
        self.destroy()

    def no_action(self):
        """Ação do botão Não"""
        self.result = False
        self.destroy()

    def center_window(self, parent):
        """Centraliza a janela em relação ao parent"""
        self.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() - self.winfo_width()) // 2
        y = parent.winfo_y() + (parent.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
