"""
Controller para gerenciar operações de Professores na GUI
"""

from app.database.repositories import professor as professor_repo
from app.exceptions.exceptions import *


class ProfessorController:
    """Controlador de operações de professores"""

    @staticmethod
    def get_all_professors():
        """Obtém todos os professores"""
        try:
            professors = professor_repo.find_all_professor()
            return professors if professors else []
        except Exception as e:
            print(f"Erro ao buscar professores: {e}")
            return []

    @staticmethod
    def get_professor_by_id(professor_id: int):
        """Obtém um professor pelo ID"""
        try:
            professor = professor_repo.find_professor_by_id(professor_id)
            return professor
        except Exception as e:
            print(f"Erro ao buscar professor: {e}")
            return None

    @staticmethod
    def create_professor(nome: str, sobrenome: str, telefone: str, cpf: str, 
                        data_nasc: str, salario: float):
        """Cria um novo professor"""
        try:
            professor_repo.insert_professor(nome, sobrenome, telefone, cpf, data_nasc, salario)
            return True
        except (CpfException, PhoneException) as e:
            print(f"Erro de validação: {e}")
            return False
        except Exception as e:
            print(f"Erro ao criar professor: {e}")
            return False

    @staticmethod
    def update_professor(professor_id: int, nome: str, sobrenome: str, telefone: str, 
                        cpf: str, data_nasc: str, salario: float):
        """Atualiza um professor"""
        try:
            professor_repo.update_professor(nome, sobrenome, telefone, cpf, data_nasc, salario, professor_id)
            return True
        except (CpfException, PhoneException) as e:
            print(f"Erro de validação: {e}")
            return False
        except Exception as e:
            print(f"Erro ao atualizar professor: {e}")
            return False

    @staticmethod
    def delete_professor(professor_id: int):
        """Deleta um professor"""
        try:
            professor_repo.delete_professor(professor_id)
            return True
        except Exception as e:
            print(f"Erro ao deletar professor: {e}")
            return False
