from datetime import datetime as dt

class Task:
    def __init__(self, deadline: str, author: str, describe: str, title:str, priority: str):
        self.deadline = dt.strptime(deadline, '%Y-%m-%d')
        self.author = author
        self.describe = describe
        self.title = title
        self.priority = priority
        self.created_at = dt.now()

    def __str__(self):
        return f'Task: {self.title} | Autor: {self.author} | Data Conclusão: {dt.strftime(self.deadline, '%d/%m/%Y')} | Dias Restantes: {len(self)}'
    
    def __len__(self):
        difference = self.deadline - self.created_at
        return difference.days + 1


#Função de Testes
def main():
    task01 = Task('2025-12-05', 'John Linn', 'Acessar documentação do Python e e revisar conteúdo.', 'Revisar Dunder Methods', 'Urgente')
    print(task01)
    print(len(task01))

if __name__ == '__main__':
    main()
    