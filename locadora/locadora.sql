create table cliente
(
    id_cliente int auto_increment,
    nome varchar(30) not null,
    telefone varchar(12),
    primary key(id_cliente)
);

create table carro
(
    id_carro int auto_increment,
    modelo varchar(15)
    marca varchar(10),        
    ano varchar(4),
    disponivel Boolean not null,   
    primary key (id_carro),
    foreign key(modelo) references tipo_carro(modelo)
);

create table tipo_carro
(
    modelo varchar(10),
    valorDiaria numeric(4,2),
    valorSemanal numeric(7,2),
    primary key(modelo)
);

create table aluguel
(
    id_cliente int,
    id_carro int,
    dataInicial date,
    dataFinal date,
    primary key(id_cliente, id_carro, dataInicial),
    foreign key(id_cliente) references cliente(id_cliente),
    foreign key(id_carro) references carro(id_carro)
);
