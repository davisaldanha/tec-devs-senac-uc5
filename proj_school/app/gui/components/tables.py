"""
Tabelas e TreeView customizadas
"""

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from app.gui.styles import (
    TABLE_BG,
    TABLE_FG,
    TABLE_HEADER_BG,
    TABLE_HEADER_FG,
    TABLE_SELECT_BG,
    FONT_TABLE,
)


class CustomTable(ctk.CTkFrame):
    """Tabela customizada usando Treeview"""

    def __init__(self, master, columns=None, height=300, **kwargs):
        super().__init__(master, **kwargs)

        self.columns = columns or []
        self.selected_row = None

        # Configurar estilo
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Custom.Treeview",
            background=TABLE_BG,
            foreground=TABLE_FG,
            fieldbackground=TABLE_BG,
            font=FONT_TABLE,
            rowheight=30,
        )
        style.configure(
            "Custom.Treeview.Heading",
            background=TABLE_HEADER_BG,
            foreground=TABLE_HEADER_FG,
            font=FONT_TABLE,
        )
        style.map("Custom.Treeview", background=[("selected", TABLE_SELECT_BG)])

        # Frame para scrollbar
        tree_frame = ctk.CTkFrame(self, fg_color="transparent")
        tree_frame.pack(fill="both", expand=True)

        # Criar Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            columns=self.columns,
            height=height // 30,
            style="Custom.Treeview",
            show="tree headings",
        )

        # Configurar colunas
        for col in self.columns:
            self.tree.column(col, width=100)
            self.tree.heading(col, text=col)

        # Scrollbars
        v_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        h_scroll = ttk.Scrollbar(
            tree_frame, orient="horizontal", command=self.tree.xview
        )

        self.tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        # Pack
        self.tree.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")

        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # Bind para seleção
        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    def insert_row(self, values):
        """Insere uma linha na tabela"""
        self.tree.insert("", "end", values=values)

    def clear(self):
        """Limpa todas as linhas da tabela"""
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_selected_row(self):
        """Retorna a linha selecionada"""
        selection = self.tree.selection()
        if selection:
            return self.tree.item(selection[0])["values"]
        return None

    def _on_select(self, event):
        """Callback de seleção"""
        selection = self.tree.selection()
        if selection:
            self.selected_row = self.tree.item(selection[0])["values"]
