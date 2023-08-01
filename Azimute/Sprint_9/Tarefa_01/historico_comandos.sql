
-- Tabela combustivel
-- começarei por ela pois a tabela carros tera que fazer referencia a ela

--cria tabela nova declarando os requesitos e a chave primaria
CREATE TABLE tb_combustivel (
  idcombustivel   int primary key,
  tipoCombustivel varchar(20)  
);

--cria tabela temporaria com informaçoes distintas da tabela Locação referente ao tipos de combustiveis 
CREATE TABLE tb_combustivel_temp AS
SELECT DISTINCT idcombustivel, tipocombustivel
from tb_locacao;

--insere os dados da tabela temporaria na tabela nova
INSERT INTO tb_combustivel SELECT * FROM tb_combustivel_temp;

--deleta a tabela temporaria
DROP TABLE tb_combustivel_temp;

-- Tabela carro
--cria a tabela carro e faz referencia de chave estrangeira a tabela combustivei
CREATE TABLE tb_carro (
  idCarro         int PRIMARY KEY,
  classiCarro     varchar(50),
  marcaCarro      varchar(80),
  modeloCarro     varchar(80),
  anoCarro        int,
  idcombustivel   int,
  FOREIGN Key (idcombustivel) REFERENCES tb_combustivel (idcombustivel)
);

--cria tabela temporaria com informaçoes distintas da tabela Locação referente ao tipos de carros
CREATE TABLE tb_carro_temp AS
SELECT DISTINCT idcarro, classicarro, marcacarro, modelocarro, anocarro, idcombustivel
from tb_locacao 
ORDER by idcarro;

--insere os dados da tabela temporaria na tabela nova
INSERT INTO tb_carro SELECT * FROM tb_carro_temp;

--deleta a tabela temporaria
DROP TABLE tb_carro_temp;

--cria Tabela cliente

CREATE TABLE tb_cliente (
  idCliente       int PRIMARY KEY,
  nomeCliente     varchar(100),
  cidadeCliente   varchar(40),
  estadoCliente   varchar(40),
  paisCliente     varchar(40)
);

--cria tabela temporaria com informaçoes distintas da tabela Locação referente ao clientes
CREATE TABLE tb_cliente_temp AS 
SELECT DISTINCT idcliente, nomecliente, cidadecliente, estadocliente, paiscliente 
FROM tb_locacao 
ORDER by idcliente;

--insere os dados da tabela temporaria na tabela nova
INSERT INTO tb_cliente SELECT * FROM tb_cliente_temp;

--deleta a tabela temporaria
DROP TABLE tb_cliente_temp;

-- cria Tabela Vendedor

CREATE TABLE tb_vendedor (
  idVendedor      int PRIMARY KEY,
  nomeVendedor    varchar(15),
  sexoVendedor    smallint,
  estadoVendedor  varchar(40)
);

--cria tabela temporaria com informaçoes distintas da tabela Locação referente aos vendedores
CREATE TABLE tb_vendedor_temp AS
SELECT DISTINCT idvendedor, nomevendedor, sexovendedor, estadovendedor
from tb_locacao;

--insere os dados da tabela temporaria na tabela nova
INSERT INTO tb_vendedor SELECT * FROM tb_vendedor_temp;

--deleta a tabela temporaria
DROP TABLE tb_vendedor_temp;

--cria nova Tabela Locação
CREATE TABLE tb_locacao_new (
  idLocacao       int primary key,
  idCliente       int,
  idCarro         int,
  kmIni           int, -- sera realizado um alias mas a frente
  dataLocacao     datetime,
  horaLocacao     time,
  qtdDiaria       int,
  vlrDiaria       decimal(18,2),
  dataEntrega     date,
  horaEntrega     time,
  idVendedor      int,
  FOREIGN Key (idCliente) REFERENCES tb_cliente (idCliente),
  FOREIGN Key (idCarro) REFERENCES tb_carro (idCarro),
  FOREIGN Key (idVendedor) REFERENCES tb_vendedor (idVendedor)
);

-- cria tabela temporaria somente com id's e dados da locação.
-- mantive kmcarro pois ela apesar de ter no nome carro não é dependêcia da tabela carros, mas sim dos status em que a locação foi realizada. 
-- por conta disto para evitar equivocos, troquei para KmIni de km Inicial.
CREATE TABLE tb_locacao_temp AS
SELECT idlocacao, idcliente, idcarro, kmcarro AS kmIni, datalocacao, horalocacao, qtddiaria, vlrdiaria, dataentrega, horaentrega, idvendedor
from tb_locacao;

--insere os dados da tabela temporaria na tabela nova
INSERT INTO tb_locacao_true SELECT * FROM tb_locacao_temp;

--deleta a tabela temporaria
DROP TABLE tb_locacao_temp;

--deleta a tabela não normalizada
DROP TABLE tb_locacao

-- renomeia nova tabela
ALTER TABLE tb_locacao_new RENAME TO tb_locacao;