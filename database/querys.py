from connection import connect

CONN = connect()

#Funções para manipular os dados  da tabela tbl_aluno
def find_student_by_id(id: int):
    '''Retornar um aluno pelo ID'''
    sql = 'SELECT * FROM tbl_aluno WHERE id_aluno = %s;'

    if CONN is not None:
        with CONN.cursor() as cur:
            try:
                # Executa a consulta SQL
                cur.execute(sql, (id,))
                return cur.fetchone()
            except Exception as e:
                print(f'Error: {e}')
                return None
        CONN.close()
    return None

def find_all_students():
    '''Retornar todos os alunos'''
    sql = 'SELECT * FROM tbl_aluno;'

    if CONN is not None:
        with CONN.cursor() as cur:
            try:
                # Executa a consulta SQL
                cur.execute(sql)
                return cur.fetchall()
            except Exception as e:
                print(f'Error: {e}')
                return None
        CONN.close()
    return None

def insert_student(nome: str, sobrenome: str, idade: int, telefone: str, cpf: str, data_nasc: str):
    '''Inserir um novo aluno'''
    