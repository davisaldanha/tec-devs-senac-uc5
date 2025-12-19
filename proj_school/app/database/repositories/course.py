from ..connection import connect
from ...validations import validations as v
from ...exceptions import *
from ...utils.utils import *
from ..queries import *

def find_course_by_id(id: int):
    '''Retornar um curso pelo ID'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_ALL_COURSE, (id,))
                    return cur.fetchone()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def find_all_courses():
    '''Retornar todos os cursos'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_ALL_COURSE)
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def insert_course(nome: str, descricao: str, carga_horaria: int):
    '''Inserir um novo curso'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(INSERT_COURSE, (nome, descricao, carga_horaria))
                    print(f'Curso {nome} cadastrado com sucesso!')
                except Exception as e:
                    print(e)
                    return None
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def update_course(nome: str, descricao: str, carga_horaria: int, id: int):
    '''Atualizar um curso'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(UPDATE_COURSE, (nome, descricao, carga_horaria, id))
                    print(f'Curso {nome} atualizado com sucesso!')
                except Exception as e:
                    print(f'Error: {e}')
                    return None

def delete_course(id: int):
    '''Deletar um curso pelo id'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    if find_course_by_id(id):
                        # Executa a consulta SQL
                        cur.execute(DELETE_COURSE, (id,))
                        print(f'Curso de ID {id} deletado com sucesso!')
                    else:
                        print(f'Curso de ID {id} não encontrado!')
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None