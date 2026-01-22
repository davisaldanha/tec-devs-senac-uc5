"""
Controller para gerenciar operações de Turmas na GUI
"""

from app.database.repositories import class_module as class_repo


class ClassController:
    """Controlador de operações de turmas"""

    @staticmethod
    def get_all_classes():
        """Obtém todas as turmas"""
        try:
            classes = class_repo.find_all_class()
            return classes if classes else []
        except Exception as e:
            print(f"Erro ao buscar turmas: {e}")
            return []

    @staticmethod
    def get_class_by_id(class_id: int):
        """Obtém uma turma pelo ID"""
        try:
            class_data = class_repo.find_class_by_id(class_id)
            return class_data
        except Exception as e:
            print(f"Erro ao buscar turma: {e}")
            return None

    @staticmethod
    def get_classes_by_professor(professor_id: int):
        """Obtém turmas de um professor"""
        try:
            classes = class_repo.find_classes_by_prof(professor_id)
            return classes if classes else []
        except Exception as e:
            print(f"Erro ao buscar turmas do professor: {e}")
            return []

    @staticmethod
    def get_classes_by_shift(shift: str):
        """Obtém turmas por turno"""
        try:
            classes = class_repo.find_classes_by_shift(shift)
            return classes if classes else []
        except Exception as e:
            print(f"Erro ao buscar turmas por turno: {e}")
            return []

    @staticmethod
    def get_classes_by_course(course_id: int):
        """Obtém turmas de um curso"""
        try:
            classes = class_repo.find_classes_by_course(course_id)
            return classes if classes else []
        except Exception as e:
            print(f"Erro ao buscar turmas do curso: {e}")
            return []

    @staticmethod
    def create_class(professor_id: int, course_id: int, shift: str):
        """Cria uma nova turma"""
        try:
            class_repo.insert_class(professor_id, course_id, shift)
            return True
        except Exception as e:
            print(f"Erro ao criar turma: {e}")
            return False

    @staticmethod
    def update_class(class_id: int, professor_id: int):
        """Atualiza uma turma"""
        try:
            class_repo.update_class(professor_id, class_id)
            return True
        except Exception as e:
            print(f"Erro ao atualizar turma: {e}")
            return False

    @staticmethod
    def delete_class(class_id: int):
        """Deleta uma turma"""
        try:
            class_repo.delete_class(class_id)
            return True
        except Exception as e:
            print(f"Erro ao deletar turma: {e}")
            return False
