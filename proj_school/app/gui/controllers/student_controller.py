"""
Controller para gerenciar operações de Alunos na GUI
Intermediária entre as views e o banco de dados
"""

from app.database.repositories import student as student_repo
from app.exceptions.exceptions import *


class StudentController:
    """Controlador de operações de alunos"""

    @staticmethod
    def get_all_students():
        """Obtém todos os alunos"""
        try:
            students = student_repo.find_all_students()
            return students if students else []
        except Exception as e:
            print(f"Erro ao buscar alunos: {e}")
            return []

    @staticmethod
    def get_student_by_id(student_id: int):
        """Obtém um aluno pelo ID"""
        try:
            student = student_repo.find_student_by_id(student_id)
            return student
        except Exception as e:
            print(f"Erro ao buscar aluno: {e}")
            return None

    @staticmethod
    def create_student(nome: str, sobrenome: str, idade: int, telefone: str, cpf: str, data_nasc: str):
        """Cria um novo aluno"""
        try:
            student_repo.insert_student(nome, sobrenome, idade, telefone, cpf, data_nasc)
            return True
        except (AgeException, CpfException, PhoneException) as e:
            print(f"Erro de validação: {e}")
            return False
        except Exception as e:
            print(f"Erro ao criar aluno: {e}")
            return False

    @staticmethod
    def update_student(student_id: int, nome: str, sobrenome: str, idade: int, 
                      telefone: str, cpf: str, data_nasc: str):
        """Atualiza um aluno"""
        try:
            student_repo.update_student(nome, sobrenome, idade, telefone, cpf, data_nasc, student_id)
            return True
        except (AgeException, CpfException, PhoneException) as e:
            print(f"Erro de validação: {e}")
            return False
        except NotFoundStudentException as e:
            print(f"Aluno não encontrado: {e}")
            return False
        except Exception as e:
            print(f"Erro ao atualizar aluno: {e}")
            return False

    @staticmethod
    def delete_student(student_id: int):
        """Deleta um aluno"""
        try:
            student_repo.delete_student(student_id)
            return True
        except NotFoundStudentException as e:
            print(f"Aluno não encontrado: {e}")
            return False
        except Exception as e:
            print(f"Erro ao deletar aluno: {e}")
            return False

    @staticmethod
    def matriculate_student(student_id: int, class_id: int):
        """Matricula um aluno em uma turma"""
        try:
            student_repo.matriculation(student_id, class_id)
            return True
        except Exception as e:
            print(f"Erro ao matricular aluno: {e}")
            return False
