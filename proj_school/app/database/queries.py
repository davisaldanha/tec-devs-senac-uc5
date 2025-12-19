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

MATRICULATION = '''UPDATE tbl_aluno SET fk_turma = %s WHERE id_aluno = %s'''


# -------------------
# -- QUERIES CLASS
# -------------------

SELECT_CLASS_ID = '''SELECT * FROM tbl_turma WHERE id_turma = %s'''

SELECT_ALL_CLASS = '''SELECT * FROM tbl_turma '''

SELECT_CLASS_PROF = '''SELECT * FROM tbl_turma WHERE fk_professor = %s'''

SELECT_CLASS_SHIFT = '''SELECT * FROM tbl_turma WHERE turno = %s'''

SELECT_CLASS_BETWEEN_DATE = '''SELECT * FROM tbl_turma WHERE criado_em BETWEEN %s AND %s'''

SELECT_CLASS_COURSE = '''SELECT * FROM tbl_turma WHERE fk_curso = %s'''

INSERT_CLASS = '''INSERT INTO tbl_turma(fk_professor, fk_curso, turno)
                    VALUES (%s, %s, %s)'''

UPDATE_CLASS = '''UPDATE tbl_turma SET fk_professor = %s WHERE id_turma = %s'''

DELETE_CLASS = '''DELETE FROM tbl_turma WHERE id_turma = %s'''

# -------------------
# -- QUERIES COURSE
# -------------------

SELECT_ALL_COURSE = 'SELECT * FROM tbl_curso'

SELECT_COURSE_ID = 'SELECT * FROM tbl_curso WHERE id_curso = %s'

INSERT_COURSE = '''INSERT INTO tbl_curso(nome, descricao, carga_horaria) VALUES (%s, %s, %s)'''

UPDATE_COURSE = '''UPDATE tbl_curso SET nome = %s, descricao = %s, carga_horaria = %s WHERE id_curso = %s'''

DELETE_COURSE = '''DELETE FROM tbl_curso WHERE id_curso = %s'''

# -------------------
# -- QUERIES PROFESSOR
# -------------------
SELECT_ALL_PROFESSOR = 'SELECT * FROM tbl_professor'

SELECT_PROFESSOR_ID = 'SELECT * FROM tbl_professor WHERE id_professor = %s'

INSERT_PROFESSOR = '''INSERT INTO tbl_professor(nome, sobrenome, telefone, cpf, data_nasc, salario)
                     VALUES (%s, %s, %s, %s, %s, %s)'''

UPDATE_PROFESSOR = '''UPDATE tbl_professor SET nome = %s, sobrenome = %s, telefone = %s, 
                        cpf = %s, data_nasc = %s, salario= %s
                        WHERE id_professor = %s'''

DELETE_PROFESSOR = '''DELETE FROM tbl_professor WHERE id_professor = %s'''

