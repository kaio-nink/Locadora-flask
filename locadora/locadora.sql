create table cliente
(
    id_cliente int auto_increment,
    nome varchar(30) not null,
    telefone varchar(12),
    primary key(id_cliente)
);

create table tipo_carro
(
    tipo varchar(15),
    valorDiaria numeric(4,2) not null,
    valorSemanal numeric(7,2) not null,
    primary key(tipo)
);

create table carro
(
    id_carro int auto_increment,
    tipo varchar(15),
    modelo varchar(15) not null,
    marca varchar(10) not null,        
    ano varchar(4) not null,
    disponivel Boolean not null,   
    primary key (id_carro),
    foreign key(tipo) references tipo_carro(tipo)
);

create table aluguel
(
    id_cliente int,
    id_carro int,
    dataInicial date,
    numDias int,
    primary key(id_cliente, id_carro, dataInicial),
    foreign key(id_cliente) references cliente(id_cliente),
    foreign key(id_carro) references carro(id_carro)
);
