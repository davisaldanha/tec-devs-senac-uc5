''' Queries que serão utilizadas no repositories'''

# -------------------
# -- QUERIES STUDENT
# -------------------

INSERT_STUDENT = '''INSERT INTO tbl_aluno(nome, sobrenome, idade, telefone, cpf, data_nasc)
                    VALUES (%s, %s, %s, %s, %s, %s);'''

UPDATE_STUDENT = '''UPDATE tbl_aluno SET nome = %s, sobrenome = %s, telefone = %s, idade = %s,
                cpf = %s, data_nasc = %s WHERE id_aluno = %s'''

DELETE_STUDENT = '''DELETE FROM tbl_aluno WHERE id_aluno = %s'''

SELECT_ALL_STUDENT = '''SELECT * FROM tbl_aluno'''

SELECT_STUDENT_ID = '''SELECT * FROM tbl_aluno WHERE id_aluno = %s'''