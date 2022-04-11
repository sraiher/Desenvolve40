# Desenvolve40+ / Magalu

## Formação com foco na linguagem Python (108 horas/aula - Let´s Code)

- Lógica de Programação
- POO
- Estrutura de Dados
- Banco de Dados

Cada um dos módulos foi encerrado com um projeto com foco nas habilidades desenvolvidas:

- black_friday 

A partir do acesso a uma arquivo dado (dados.jso) com uma lista de dicionários, onde cada dicionário representa um produto com: 
ID (identificador único), o preço e a categoria do produto. 

Funções implementadas: listar todas as categorias, listar todos os produtos de uma categoria, identificar o produto mais barato e o mais caro de uma categoria e o top 10 de produtos mais baratos e mais caros de toda a base de dados.

- loja_bike

Sistema de Empréstimo de Bicicletas a partir de duas classes principais (Cliente, Loja).

Cliente pode: • Ver as bicicletas disponíveis na Loja; • Alugar bicicletas por hora (R$5/hora); • Alugar bicicletas por dia (R$25/dia); • Alugar bicicletas por semana (R$100/semana)• Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquertipo) com 30% de desconto no valor total.

Loja pode: • Calcular a conta quando o cliente decidir devolver a bicicleta; • Mostrar o estoque de bicicletas; • Receber pedidos de aluguéis por hora, diários ou semanais validando apossibilidade com o estoque e modo de aluguel existente. • Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana); 
 • O cliente pode decidir livremente quantas bicicletas quer alugar; • Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis.

- busca_rios

Dada uma lista bi-dimensional com altura e largura não necessáriamente iguais contendo apenas 0's e 1's. 
Cada 1 representa um pedaço de rio, enquanto os 0's representam terra. Rios são compostos por 1's adjacentes horizontalmente ou verticalmente (mas não diagonalmente). 
O número de 1's adjacentes representa o tamanho do rio.

O rio pode fazer curvas, isto é, rios podem ter formato de L ou até mesmo de cruz e são considerados um rio só.

Criado um algoritmo que recebe esta lista bi-dimensional e retorna uma lista com os tamanhos dos rios dentro dessa estrutura, os tamanhos de rios dentro da lista resposta não precisam ter uma ordem específica.

- escola

Dados modelo entidade relacinal e um modelo relacional a partir do DER: 

1.	Implementar um script SQL chamado ‘escola.sql’ com os comandos de criação do banco de dados escola.

  a.	Criar um banco de dados vazio chamado escola.
  b.	Criar todas as tabelas que fazem parte do banco, a partir do modelo relacional.
  c.	Definir as restrições de integridade referencial (chaves estrangeiras) nas tabelas necessárias.
  d.	Definir as chaves primárias das tabelas.
  e.	Definir as restrições de domínio de atributo.
  f.	Conter comandos de inserção de dados em todas as tabelas. Os dados inseridos serão utilizados na etapa 2 do projeto.

2.	Implementar um script SQL chamado ‘consultas_escola.sql’ com os comandos que respondam às seguintes consultas:

  a.	Produza um relatório que contenha os dados dos alunos matriculados em todos os cursos oferecidos pela escola.
  b.	Produza um relatório com os dados de todos os cursos, com suas respectivas disciplinas, oferecidos pela escola.
  c.	Produza um relatório que contenha o nome dos alunos e as disciplinas em que estão matriculados.
  d.	Produza um relatório com os dados dos professores e as disciplinas que ministram.
  e.	Produza um relatório com os nomes das disciplinas e seus pré-requisitos.
  f.	Produza um relatório com a média de idade dos alunos matriculados em cada curso.
  g.	Produza um relatório com os cursos oferecidos por cada departamento.

Considere que:

1.	O SGBD adotado para o projeto deve ser o MySQL.
2.	Os scripts devem ser implementados de modo que sua execução seja direta e aconteça sem erros em qualquer ambiente MySQL.
3.	O domínio dos atributos (tipo de dados, formato, etc.) fica a critério do aluno.
4.	O aluno tem liberdade de criar novos atributos ou relações que julgar necessário para enriquecimento do modelo.

