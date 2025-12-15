from connection import connect
from validations import validations as v
from exceptions.exceptions import *

#Funções para manipular os dados  da tabela tbl_aluno
def find_student_by_id(id: int):
    '''Retornar um aluno pelo ID'''
    sql = 'SELECT * FROM tbl_aluno WHERE id_aluno = %s;'

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(sql, (id,))
                    return cur.fetchone()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def find_all_students():
    '''Retornar todos os alunos'''
    sql = 'SELECT * FROM tbl_aluno;'

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    # Executa a consulta SQL
                    cur.execute(sql)
                    return cur.fetchall()
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None

def insert_student(nome: str, sobrenome: str, idade: int, telefone: str, cpf: str, data_nasc: str):
    '''Inserir um novo aluno'''
    sql = '''
            INSERT INTO tbl_aluno(nome, sobrenome, idade, telefone, cpf, data_nasc)
            VALUES (%s, %s, %s, %s, %s, %s);
        '''
    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    #Valida os valores dos argumentos
                    v.validation_age(idade)
                    v.validation_cpf(cpf)
                    v.validation_phone(telefone)
                    # Executa a consulta SQL
                    cur.execute(sql, (nome, sobrenome, idade, telefone, cpf, data_nasc))
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
    sql = 'DELETE FROM tbl_aluno WHERE id_aluno = %s;'

    with connect() as CONN:
        if CONN is not None:
            with CONN.cursor() as cur:
                try:
                    if find_student_by_id(id):
                        # Executa a consulta SQL
                        cur.execute(sql, (id,))
                        print('Aluno excluído com sucesso!')
                        return
                    raise NotFoundStudentException(f'Aluno com ID {id} não foi encontrado!')
                except Exception as e:
                    print(f'Error: {e}')
                    return None
        return None
    