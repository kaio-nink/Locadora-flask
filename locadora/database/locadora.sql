create database if not exists Locadora;
use Locadora;


create table if not exists Cliente
(
    id_cliente int auto_increment,
    nome varchar(30) not null,
    telefone varchar(12),
    primary key(id_cliente)
);

create table if not exists Tipo_carro
(
    tipo varchar(15),
    valorDiaria numeric(4,2) not null,
    valorSemanal numeric(7,2) not null,
    primary key(tipo)
);

create table if not exists Carro
(
    id_carro int auto_increment,
    tipo varchar(15),
    modelo varchar(15) not null,
    marca varchar(10) not null,        
    ano varchar(4) not null,
    disponivel Boolean not null,   
    primary key (id_carro),
    foreign key(tipo) references Tipo_carro(tipo)
);

create table if not exists Aluguel
(
    id_cliente int,
    id_carro int,
    dataInicial date,
    numDias int,
    primary key(id_cliente, id_carro, dataInicial),
    foreign key(id_cliente) references Cliente(id_cliente),
    foreign key(id_carro) references Carro(id_carro)
);

alter table Cliente auto_increment=1;
alter table Carro auto_increment=1;


delimiter ;;
create procedure cadastrarCliente(in nome varchar(30), in telefone varchar(12))
    begin
        insert into Cliente(nome, telefone) values(nome, telefone);
    end;;


delimiter ;;
create procedure cadastrarCarro(in tipo varchar(15), in modelo varchar(15), in marca varchar(10), in ano varchar(4), in disponivel boolean)
    begin
        insert into Carro(tipo, modelo, marca, ano, disponivel) values(tipo, modelo, marca, ano, disponivel);
    end;;
