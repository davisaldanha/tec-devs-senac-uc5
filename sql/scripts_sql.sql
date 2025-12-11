-- COMANDOS DDL: LINGUAGEM DE DEFINIÇÃO DE DADOS
/*
	CREATE: CRIAR
	ALTER: ALTERAR/MODIFICAR
	DROP: EXCLUIR


	constraints: PRIMARY KEY, NOT NULL, DEFAULT, UNIQUE
*/

-- Tabela para representar um aluno
CREATE TABLE tbl_aluno(
	id_aluno SERIAL PRIMARY KEY,
	nome VARCHAR(15) NOT NULL,
	sobrenome VARCHAR(45) NOT NULL,
	idade INT NOT NULL,
	telefone VARCHAR(11) NOT NULL,
	cpf VARCHAR(11) NOT NULL,
	data_nasc DATE NOT NULL,
	criado_em DATE DEFAULT CURRENT_DATE
)
-- Tabela para representar o professor

CREATE TABLE tbl_professor(
	id_professor SERIAL PRIMARY KEY,
	nome VARCHAR(15) NOT NULL,
	sobrenome VARCHAR(45) NOT NULL,
	telefone VARCHAR(11) NOT NULL,
	cpf VARCHAR(11) NOT NULL,
	data_nasc DATE NOT NULL,
	criado_em DATE DEFAULT CURRENT_DATE,
	salario DECIMAL(10, 2) NOT NULL
)

-- Alterar as tabelas adicionando UNIQUE para as colunas cpf.
ALTER TABLE tbl_aluno ADD CONSTRAINT tbl_aluno_uniqueCpf
UNIQUE (cpf);

ALTER TABLE tbl_professor ADD CONSTRAINT tbl_professor_uniqueCpf
UNIQUE (cpf);

-- Tabela para representar um curso
CREATE TABLE tbl_curso(
	id_curso SERIAL PRIMARY KEY,
	nome VARCHAR(45) NOT NULL,
	descricao TEXT DEFAULT 'Sem informações adicionais',
	carga_horaria INT NOT NULL,
	criado_em DATE DEFAULT CURRENT_DATE
);

-- Tabela para representar uma turma 
CREATE TABLE tbl_turma(
	id_turma SERIAL PRIMARY KEY,
	fk_professor INT NOT NULL,
	fk_curso INT NOT NULL,
	turno VARCHAR(10) NOT NULL,
	criado_em DATE DEFAULT CURRENT_DATE,
	FOREIGN KEY (fk_professor) REFERENCES tbl_professor(id_professor),
	FOREIGN KEY (fk_curso) REFERENCES tbl_curso(id_curso)
);

-- Adicionar uma nova coluna em tbl_aluno por nome fk_turma
ALTER TABLE tbl_aluno ADD COLUMN fk_turma INT REFERENCES tbl_turma(id_turma);

/*
	COMANDOS DML: LINGUAGEM DE MANIPULAÇÃO DE DADOS

	INSERT INTO: Cadastrar instâncias de dados nas tabelas
	UPDATE SET: Atualizar os dados
	DELETE FROM: Excluir os dados
*/

-- Inserção de dados na tabela tbl_curso
INSERT INTO tbl_curso(nome, descricao, carga_horaria) VALUES 
('Analista de Dados', NULL, 240),
('Formação Python', 'Se torne um desenvolvedor expert em Python.', 156),
('Power BI com Copilot', 'Aprenda a criar dashboards interativos com IA.', 40);

SELECT * FROM tbl_curso;

-- Inserção de dados na tabela tbl_aluno
INSERT INTO tbl_aluno(nome, sobrenome, idade, telefone, cpf, data_nasc) VALUES
('Mario', 'Bros', 25, '85900000000', '22233344411', '2000-01-01'),
('Maria', 'Joaquina', 24, '85911111111', '11122233344', '2001-02-02'),
('João', 'Carlos', 20, '85922222222', '99988877711', '2005-05-06'),
('Maria', 'Clara', 19, '85933333333', '33344455571', '2006-12-12'),
('Rafael', 'Marques', 15, '85955566666', '00099988812', '2010-01-23');

SELECT * FROM tbl_aluno;

-- Inserção de dados na tabela tbl_professor

INSERT INTO tbl_professor (nome, sobrenome, telefone, cpf, data_nasc, salario)
VALUES
('Carlos', 'Almeida', '85987654321', '12345678901', '1980-05-12', 4500.00),
('Mariana', 'Silva Costa', '85999887766', '23456789012', '1985-09-23', 5200.00),
('João', 'Pereira Santos', '85991234567', '34567890123', '1978-02-17', 6100.00),
('Fernanda', 'Oliveira Lima', '85993456789', '45678901234', '1990-11-05', 4800.00),
('Ricardo', 'Mendes Rocha', '85994561234', '56789012345', '1983-07-30', 5300.00);

SELECT * FROM tbl_professor;

