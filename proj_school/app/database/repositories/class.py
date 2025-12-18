from ..connection import connect
from ...validations import validations as v
from ...exceptions import *
from ...utils.utils import *
from ..queries import *

def find_class_by_id(id: int):
    '''Retorna uma turma pelo ID'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_CLASS_ID, (id,))
                    return cur.fetchone()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def find_all_class():
    '''Retorna as turmas cadastradas'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_ALL_CLASS)
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def find_classes_by_prof(id_professor: int):
     '''Retorna turmas por professor'''
     with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_CLASS_PROF, (id_professor,))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def find_classes_by_shift(shift: str):
    '''Retorna turmas por turno'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_CLASS_SHIFT, (shift,))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def find_classes_between_date(initial_date, final_date):
    '''Retorna as turmas por data inicial e final'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_CLASS_BETWEEN_DATE, (initial_date, final_date))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def find_classes_by_course(id_course: int):
    '''Retorna turmas por curso'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_CLASS_COURSE, (id_course))
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def insert_class(id_professor: int, id_course: int, shift: str):
    '''Cadastrar uma nova turma'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(INSERT_CLASS, (id_professor, id_course, shift))
                    return
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def update_class(id_professor: int, id_class: int):
    '''Atualizar o professor de um turma'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(UPDATE_CLASS, (id_professor, id_class))
                    return
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def delete_class(id_class):
    '''Deletar uma turma'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(DELETE_CLASS, (id_class, ))
                    return
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None