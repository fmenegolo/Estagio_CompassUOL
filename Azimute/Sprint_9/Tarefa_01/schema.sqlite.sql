-- TABLE
CREATE TABLE tb_carro (
  idCarro         int PRIMARY KEY,
  classiCarro     varchar(50),
  marcaCarro      varchar(80),
  modeloCarro     varchar(80),
  anoCarro        int,
  idcombustivel   int,
  FOREIGN Key (idcombustivel) REFERENCES tb_combustivel (idcombustivel)
);
CREATE TABLE tb_cliente (
  idCliente       int PRIMARY KEY,
  nomeCliente     varchar(100),
  cidadeCliente   varchar(40),
  estadoCliente   varchar(40),
  paisCliente     varchar(40)
);
CREATE TABLE "tb_combustivel" (
  idcombustivel   int primary key,
  tipoCombustivel varchar(20)  
);
CREATE TABLE "tb_locacao" (
  idLocacao       int primary key,
  idCliente       int,
  idCarro         int,
  kmIni           int,
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
CREATE TABLE tb_vendedor (
  idVendedor      int PRIMARY KEY,
  nomeVendedor    varchar(15),
  sexoVendedor    smallint,
  estadoVendedor  varchar(40)
);
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
