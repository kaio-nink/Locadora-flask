create database if not exists Locadora;
use Locadora;


create table if not exists Cliente
(
    id_cliente int auto_increment,
    nome varchar(30) not null,
    telefone varchar(12),
    primary key(id_cliente)
);

create table if not exists Categoria_veiculo
(
    categoria varchar(15),
    valorDiaria numeric(5,2) not null,
    valorSemanal numeric(7,2) not null,
    primary key(categoria)
);

create table if not exists Veiculo
(
    id_veiculo int auto_increment,
    marca varchar(10) not null,   
    modelo varchar(15) not null,
    categoria varchar(15),
    ano varchar(4) not null,
    disponivel Boolean not null default TRUE,   
    primary key (id_veiculo),
    foreign key(categoria) references Categoria_veiculo(categoria)
);

create table if not exists Aluguel
(
    id_cliente int,
    id_veiculo int,
    dataInicial date,
    numDias int,
    pendente boolean default TRUE,
    primary key(id_cliente, id_veiculo, dataInicial),
    foreign key(id_cliente) references Cliente(id_cliente),
    foreign key(id_veiculo) references Veiculo(id_veiculo)
);