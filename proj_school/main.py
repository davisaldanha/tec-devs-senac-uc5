from app.gui.main_window import MainWindow


def main():
    """
    Função principal da aplicação
    Inicia a interface gráfica com CustomTkinter
    """
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()