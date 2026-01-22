import customtkinter as ctk

class CardFrame(ctk.CTkFrame):
    """Frame customizado para exibir cards informativos"""

    def __init__(self, master, title="", **kwargs):
        super().__init__(
            master,
            fg_color="white",
            corner_radius=10,
            border_width=1,
            border_color="#E0E0E0",
            **kwargs,
        )

        # Título do card
        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 16, "bold"),
            text_color="#333333",
        )
        title_label.pack(padx=15, pady=(15, 10), anchor="w")

        # Frame de conteúdo
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    def get_content_frame(self):
        """Retorna o frame de conteúdo para adicionar widgets"""
        return self.content_frame
    
class CustomFrame(ctk.CTkFrame):
    """Frame customizado com padding padrão"""

    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            fg_color="white",
            corner_radius=8,
            border_width=1,
            border_color="#D0D0D0",
            **kwargs,
        )

class SectionFrame(ctk.CTkFrame):
    """Frame para seções distintas na interface"""

    def __init__(self, master, title="", **kwargs):
        super().__init__(
            master,
            fg_color="#F9F9F9",
            corner_radius=8,
            border_width=1,
            border_color="#E0E0E0",
            **kwargs,
        )

        if title:
            title_label = ctk.CTkLabel(
                self,
                text=title,
                font=("Segoe UI", 14, "bold"),
                text_color="#444444",
            )
            title_label.pack(padx=10, pady=(10, 5), anchor="w")
    
    def get_content_frame(self):
        """Retorna o frame de conteúdo para adicionar widgets"""
        return self