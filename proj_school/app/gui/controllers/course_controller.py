"""
Controller para gerenciar operações de Cursos na GUI
"""

from app.database.repositories import course as course_repo


class CourseController:
    """Controlador de operações de cursos"""

    @staticmethod
    def get_all_courses():
        """Obtém todos os cursos"""
        try:
            courses = course_repo.find_all_courses()
            return courses if courses else []
        except Exception as e:
            print(f"Erro ao buscar cursos: {e}")
            return []

    @staticmethod
    def get_course_by_id(course_id: int):
        """Obtém um curso pelo ID"""
        try:
            course = course_repo.find_course_by_id(course_id)
            return course
        except Exception as e:
            print(f"Erro ao buscar curso: {e}")
            return None

    @staticmethod
    def create_course(nome: str, descricao: str, carga_horaria: int):
        """Cria um novo curso"""
        try:
            course_repo.insert_course(nome, descricao, carga_horaria)
            return True
        except Exception as e:
            print(f"Erro ao criar curso: {e}")
            return False

    @staticmethod
    def update_course(course_id: int, nome: str, descricao: str, carga_horaria: int):
        """Atualiza um curso"""
        try:
            course_repo.update_course(nome, descricao, carga_horaria, course_id)
            return True
        except Exception as e:
            print(f"Erro ao atualizar curso: {e}")
            return False

    @staticmethod
    def delete_course(course_id: int):
        """Deleta um curso"""
        try:
            course_repo.delete_course(course_id)
            return True
        except Exception as e:
            print(f"Erro ao deletar curso: {e}")
            return False
