use escola;

-- a. Criar um banco de dados vazio chamado escola. 

CREATE DATABASE escola;

/*b. Criar todas as tabelas que fazem parte do banco, a partir do modelo relacional.
  c. Definir as restrições de integridade referencial (chaves estrangeiras) na tabela relacional.
  d. Definir as chaves primárias das tabelascustomer_customer_democustomer_customer_demo
*/

CREATE TABLE depto (
    codigo INTEGER AUTO_INCREMENT,
    nome VARCHAR(50),
    PRIMARY KEY (codigo)
);

/*
INSERT INTO depto (nome)
VALUES ('Matematica');
INSERT INTO depto (nome)
VALUES ('Musica');
*/

CREATE TABLE curso (
    codigo INTEGER AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT,
    codigo_depto INTEGER NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (codigo_depto)
        REFERENCES depto (codigo)
);

/*
INSERT INTO curso (nome, codigo_depto)
VALUES ('Formacao', 2);
INSERT INTO curso (nome, codigo_depto)
VALUES ('Pos Graduacao', 2);
INSERT INTO curso (nome, codigo_depto)
VALUES ('Curso Livre', 2);

UPDATE curso SET nome = 'Formacao'
WHERE codigo = 1;
*/

CREATE TABLE prof (
    matricula INTEGER AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    endereco VARCHAR(50),
    tel CHAR(11),
    data_nasc DATE,
    email VARCHAR(50),
    data_contrato DATE,
    codigo_depto INTEGER NOT NULL,
    PRIMARY KEY (matricula),
    FOREIGN KEY (codigo_depto)
        REFERENCES depto (codigo)
);

/*
INSERT INTO prof (nome, endereco, tel, data_nasc, email, data_contrato, codigo_depto)
VALUES ('Matheus', 'Rua do Sobe e Desce, s/n,', 
'11986360087', '1983-04-15', 'matheus@lets.com', '2022-01-01', 1);
INSERT INTO prof (nome, endereco, tel, data_nasc, email, data_contrato, codigo_depto)
VALUES ('Fernando', 'Rua do Desce e Sobe, s/n,', 
'11981234087', '1990-01-21', 'fernando@lets.com', '2021-05-01', 1);
INSERT INTO prof (nome, endereco, tel, data_nasc, email, data_contrato, codigo_depto)
VALUES ('Gisella', 'Rua do Sobe e Sobe, s/n,', 
'12386360087', '1965-07-02', 'gisella@lets.com', '2015-06-15', 2);
INSERT INTO prof (nome, endereco, tel, data_nasc, email, data_contrato, codigo_depto)
VALUES ('Toninho', 'Rua do Desce e Desce, s/n,', 
'12386362154', '1964-04-01', 'toninho@lets.com', '2016-03-25', 2);
*/

CREATE TABLE disc (
    codigo INTEGER AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    qtd_cred BIGINT NOT NULL,
    matri_prof INTEGER NOT NULL,
    PRIMARY KEY (codigo),
    FOREIGN KEY (matri_prof)
        REFERENCES prof (matricula)
);

/*
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Calculo', 50, 1);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Algebra', 50, 1);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Trigonometria', 20, 2);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Estatistica', 30, 2);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Canto', 20, 2);
UPDATE disc SET matri_prof= 3
WHERE codigo = 3;
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Saxofone', 30, 2);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Teclado', 20, 3);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Violao', 30, 4);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Geometria Analitica', 20, 1);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Guitarra', 30, 3);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Trigonometria', 50, 2);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Geometria', 20, 1);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Geometria Analitica', 30, 2);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Canto', 50, 3);
INSERT INTO disc(nome, qtd_cred, matri_prof)
VALUES ('Teclado', 20, 4);
*/

CREATE TABLE compoe (
    id INTEGER AUTO_INCREMENT,
    codigo_curso INTEGER NOT NULL,
    codigo_di INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (codigo_curso)
        REFERENCES curso (codigo),
    FOREIGN KEY (codigo_di)
        REFERENCES disc (codigo)
);

/*
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (1, 2);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (2, 9);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (3, 1);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (1, 8);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (2, 4);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (3, 10);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (1, 11);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (1, 3);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (2, 12);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (2, 5);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (3, 7);
INSERT INTO compoe(codigo_curso, codigo_di)
VALUES (3, 6);
*/

CREATE TABLE pre_req (
    id INTEGER AUTO_INCREMENT,
    codigo_disci INTEGER NOT NULL,
    codigo_disc_dependencia INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (codigo_disci)
        REFERENCES disc (codigo),
    FOREIGN KEY (codigo_disc_dependencia)
        REFERENCES disc (codigo)
);

-- ALTER TABLE pre_req DROP COLUMN id; (totalmente dispensável)

/*
INSERT INTO pre_req(codigo_disci, codigo_disc_dependencia)
VALUES (2, 1);
INSERT INTO pre_req(codigo_disci, codigo_disc_dependencia)
VALUES (9, 8);
INSERT INTO pre_req(codigo_disci, codigo_disc_dependencia)
VALUES (11, 12);
INSERT INTO pre_req(codigo_disci, codigo_disc_dependencia)
VALUES (5, 6);
INSERT INTO pre_req(codigo_disci, codigo_disc_dependencia)
VALUES (7, 3);
INSERT INTO pre_req(codigo_disci, codigo_disc_dependencia)
VALUES (4, 10);
*/

CREATE TABLE aluno (
    cpf CHAR(11) NOT NULL,
    nome VARCHAR(30) NOT NULL,
    endereco VARCHAR(50),
    tel CHAR(11) NOT NULL,
    data_nasc DATE,
    email VARCHAR(50) NOT NULL,
    PRIMARY KEY (cpf)
);

/*
INSERT INTO aluno (cpf, nome, endereco, tel, data_nasc, email)
VALUES ('02262814857', 'Sandra Raiher', 'Alameda dos Uapes, 36', 
'11986360097', '1964-04-01', 'sraiher@gmail.com');
INSERT INTO aluno (cpf, nome, endereco, tel, data_nasc, email)
VALUES ('02123814857', 'Caio Raiher', 'Alameda dos Uapes, 36', 
'11981230097', '1986-01-22', 'craiher@gmail.com');
INSERT INTO aluno (cpf, nome, endereco, tel, data_nasc, email)
VALUES ('02262123456', 'Martha Raiher', 'Alameda dos Uapes, 36', 
'11986123456', '1983-08-25', 'mraiher@gmail.com');
INSERT INTO aluno (cpf, nome, endereco, tel, data_nasc, email)
VALUES ('01234564857', 'Ana Clara Raiher', 'Alameda dos Uapes, 36', 
'18191234597', '2010-03-04', 'anaraiher@gmail.com');
INSERT INTO aluno (cpf, nome, endereco, tel, data_nasc, email)
VALUES ('84523697852', 'Eliana Reis', 'Alameda dos Uapes, 36', 
'11254789637', '1965-12-25', 'eliana@gmail.com');
INSERT INTO aluno (cpf, nome, endereco, tel, data_nasc, email)
VALUES ('32548752312', 'Luciano Silva', 'Alameda dos Uapes, 36', 
'11251457856', '1962-06-12', 'luciano@gmail.com');
*/

CREATE TABLE matricula (
    data_matricula DATE,
    cpf_aluno CHAR(11),
    codigo_curso INTEGER,
    FOREIGN KEY (cpf_aluno)
        REFERENCES aluno (cpf),
    FOREIGN KEY (codigo_curso)
        REFERENCES curso (codigo)
);

/*
INSERT INTO matricula(data_matricula, cpf_aluno, codigo_curso)
VALUES ('2020-01-15', '02262814857', 3);
INSERT INTO matricula(data_matricula, cpf_aluno, codigo_curso)
VALUES ('2020-01-12', '02123814857', 2);
INSERT INTO matricula(data_matricula, cpf_aluno, codigo_curso)
VALUES ('2020-01-20', '01234564857', 1);
INSERT INTO matricula(data_matricula, cpf_aluno, codigo_curso)
VALUES ('2020-01-16', '01234564857', 2);
INSERT INTO matricula(data_matricula, cpf_aluno, codigo_curso)
VALUES ('2020-01-16', '84523697852', 3);
INSERT INTO matricula(data_matricula, cpf_aluno, codigo_curso)
VALUES ('2020-01-16', '32548752312', 1);
*/

CREATE TABLE cursa (
    cpf_aluno CHAR(11),
    codigo_disc INT,
    FOREIGN KEY (cpf_aluno)
        REFERENCES aluno (cpf),
    FOREIGN KEY (codigo_disc)
        REFERENCES disc (codigo)
);

/*
INSERT INTO cursa (cpf_aluno, codigo_disc)
VALUES ('02262814857', 2);
INSERT INTO cursa (cpf_aluno, codigo_disc)
VALUES ('02262814857', 9);
INSERT INTO cursa (cpf_aluno, codigo_disc)
VALUES ('01234564857', 1);
INSERT INTO cursa (cpf_aluno, codigo_disc)
VALUES ('01234564857', 8);
INSERT INTO cursa (cpf_aluno, codigo_disc)
VALUES ('84523697852', 5);
INSERT INTO cursa (cpf_aluno, codigo_disc)
VALUES ('32548752312', 12);
*/

SELECT * FROM aluno;
SELECT * FROM depto;
SELECT * FROM curso;
SELECT * FROM prof;
SELECT * FROM matricula;
SELECT * FROM disc;
SELECT * FROM cursa;
SELECT * FROM compoe; 
SELECT * FROM pre_req;

-- 2. Implementar um script SQL chamado 'consultas_escola.sql' com os comandos que respondam às seguintes consultas:

-- a. Produza um relatório que contenha os dados dos alunos matriculados em todos os cursos oferecidos pela escola.

SELECT 
    a.nome Nome, cpf, endereco, tel, data_nasc, email
FROM
    aluno a
        INNER JOIN
    matricula m ON a.cpf = m.cpf_aluno
        INNER JOIN
    cursa c ON c.codigo_disc = m.codigo_curso
ORDER BY a.nome;

-- b. Produza um relatório com os dados de todos os cursos, com suas respectivas disciplinas, oferecidos pela escola.

SELECT 
    c.nome Nome, d.nome Disciplina
FROM
    curso c
        INNER JOIN
    compoe cm ON c.codigo = cm.codigo_curso
        INNER JOIN
    disc d ON d.codigo = cm.codigo_di
ORDER BY codigo_curso;

-- c. Produza um relatório que contenha o nome dos alunos e as disciplinas em que estão matriculados.

SELECT 
    a.nome Nome, d.nome Disciplina
FROM
    aluno a
        INNER JOIN
    cursa c ON c.cpf_aluno = a.cpf
        INNER JOIN
    disc d ON d.codigo = c.codigo_disc
ORDER BY a.nome;

-- d. Produza um relatório com os dados dos professores e as disciplinas que ministram.

SELECT 
    p.nome Nome, d.nome Disciplina
FROM
    prof p
        INNER JOIN
    disc d ON d.matri_prof = p.matricula
ORDER BY p.nome;

-- e. Produza um relatório com os nomes das disciplinas e seus pré-requisitos.

SELECT 
    d.nome Disciplina, pre.codigo_disc_dependencia Dependencia
FROM 
    disc d
        INNER JOIN
    pre_req pre ON d.codigo = pre.codigo_disci;
    
 USE escola;
SELECT 
    (SELECT 
		disciplina.nome_disciplina
        FROM
		disciplina
        WHERE
		disciplina.codigo_disciplina = pre_req.codigo_disciplina) 'DISCIPLINA',
		disciplina.nome_disciplina 'DEPENDENCIA'
FROM
    pre_req
        INNER JOIN
    disciplina ON disciplina.codigo_disciplina = pre_req.codigo_disciplina_dependencia
ORDER BY disciplina.nome_disciplina;   
    
    
    
    
    
    
    
    

-- f. Produza um relatório com a média das idades dos alunos matriculados em cada curso.

SELECT 
    FLOOR(AVG(DATEDIFF(CURRENT_DATE(), aluno.data_nasc) / 365)) AS 'Media_idade'
FROM
    aluno
; 

-- g. Produza um relatório com os cursos oferecidos em cada departamento.

SELECT 
    d.nome Departamento, c.nome Nome_Curso
FROM
    curso c
        INNER JOIN
    depto d ON d.codigo = c.codigo_depto;