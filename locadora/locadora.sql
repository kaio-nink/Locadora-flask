create table cliente
(
    id_cliente int,
    nome varchar(30) not null,
    telefone varchar(11),
    primary key(id_cliente)
);

create table carro
(
    id_carro int,
    disponivel Boolean not null,
    primary key (id_carro)
);

create table tipo_carro
(
    id_carro int,
    modelo varchar(10),
    marca varchar(10),
    ano varchar(4),
    valorDiaria numeric(4,2),
    primary key(id_carro, modelo),
    foreign key(id_carro) references carro(id_carro)
);

create table aluguel
(
    id_cliente int,
    id_carro int,
    dataInicial date,
    primary key(id_cliente, id_carro, dataInicial),
    foreign key(id_cliente) references cliente(id_cliente),
    foreign key(id_carro) references carro(id_carro)
);