from ..connection import connect
from ...validations import validations as v
from ...exceptions import *
from ...utils.utils import *
from ..queries import *

def find_professor_by_id(id: int):
    '''Retornar um professor pelo ID'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_ALL_PROFESSOR, (id,))
                    return cur.fetchone()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def find_all_professor():
    '''Retornar todos os professores'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_ALL_PROFESSOR)
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def insert_professor(nome, sobrenome, telefone, cpf, data_nasc, salario):
    '''Inserir um novo professor'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    #Valida os valores dos argumentos
                    v.validation_cpf(cpf)
                    v.validation_phone(telefone)
                    # Executa a consulta SQL
                    cur.execute(INSERT_PROFESSOR, (nome, sobrenome, telefone, cpf, convert_date(data_nasc)), salario)
                    print(f'Aluno {nome} cadastrado com sucesso!')
                except (CpfException, PhoneException) as e:
                    print(e)
                    return None
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        
        return None
    
def update_professor(nome, sobrenome, telefone, cpf, data_nasc, salario, id):
    '''Atualizar um professor'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    #Valida os valores dos argumentos
                    v.validation_cpf(cpf)
                    v.validation_phone(telefone)
                    # Executa a consulta SQL
                    cur.execute(UPDATE_PROFESSOR, (nome, sobrenome, telefone, cpf, convert_date(data_nasc)), salario, id)
                    print(f'Aluno {nome} atualizado com sucesso!')
                except (CpfException, PhoneException) as e:
                    print(e)
                    return None
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        
        return None
    
def delete_professor(id):
    '''Deletar um professor pelo id'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    if find_professor_by_id(id):
                        # Executa a consulta SQL
                        cur.execute(DELETE_PROFESSOR, (id,))
                        print('Professor excluído com sucesso!')
                        return
                    raise NotFoundStudentException(f'Professor com ID {id} não foi encontrado!')
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
