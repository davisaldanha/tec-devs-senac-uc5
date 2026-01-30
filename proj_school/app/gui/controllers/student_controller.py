'''
Controller para gerenciar operações de ALunos na GUI
Intermediário entre as views e o banco de dados
'''
from app.database.repositories import student as student_repo

class StudentController:

    @staticmethod
    def get_all_students():
        '''Obtém todos os alunos'''
        try:
            students = student_repo.find_all_students()
            return students if students else []
        except Exception as e:
            print(f'Erro ao buscar os alunos: {e}')
            return []