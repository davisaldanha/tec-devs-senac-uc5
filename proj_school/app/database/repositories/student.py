from ..connection import connect
from ...validations import validations as v
from ...exceptions import *
from ...utils.utils import *
from ..queries import *

#Funções para manipular os dados  da tabela tbl_aluno
def find_student_by_id(id: int):
    '''Retornar um aluno pelo ID'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_STUDENT_ID, (id,))
                    return cur.fetchone()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def find_all_students():
    '''Retornar todos os alunos'''

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(SELECT_ALL_STUDENT)
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def insert_student(nome: str, sobrenome: str, idade: int, telefone: str, cpf: str, data_nasc: str):
    '''Inserir um novo aluno'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    #Valida os valores dos argumentos
                    v.validation_age(idade)
                    v.validation_cpf(cpf)
                    v.validation_phone(telefone)
                    # Executa a consulta SQL
                    cur.execute(INSERT_STUDENT, (nome, sobrenome, idade, telefone, cpf, convert_date(data_nasc)))
                    print(f'Aluno {nome} cadastrado com sucesso!')
                except (AgeException, CpfException, PhoneException) as e:
                    print(e)
                    return None
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        
        return None
    
def delete_student(id: int):
    '''Deletar um aluno pelo id'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    if find_student_by_id(id):
                        # Executa a consulta SQL
                        cur.execute(DELETE_STUDENT, (id,))
                        print('Aluno excluído com sucesso!')
                        return
                    raise NotFoundStudentException(f'Aluno com ID {id} não foi encontrado!')
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    
def update_student(nome: str, sobrenome: str, idade: int, 
                   telefone: str, cpf: str, data_nasc: str, id: int):
    '''Atualiza um aluno à partir do id'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    if find_student_by_id(id):
                        #Valida os valores dos argumentos
                        v.validation_age(idade)
                        v.validation_cpf(cpf)
                        v.validation_phone(telefone)
                        # Executa a consulta SQL
                        cur.execute(UPDATE_STUDENT, (nome, sobrenome, telefone, idade, cpf, convert_date(data_nasc), id))
                        print("Aluno atualizado com sucesso!")
                        return
                    raise NotFoundStudentException(f'Aluno com ID {id} não foi encontrado!')
                except (AgeException, CpfException, PhoneException) as e:
                    print(e)
                    return None
                except Exception as e:
                    print(f'Error: {e}')

def matriculation(id_student: int, id_turma: int):
    '''Realiza a matricula de um aluno em uma turma'''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    if find_student_by_id(id_student):
                        #Executa a query
                        cur.execute(MATRICULATION, (id_student, id_turma))
                        print('Matricula realizada com sucesso!')
                        return
                    raise NotFoundStudentException(f'Aluno com ID {id} não foi encontrado!')
                except Exception as e:
                    print(e)
                    return None
