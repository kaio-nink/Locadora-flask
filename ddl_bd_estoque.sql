create table produto (
    id_produto int,
    nome varchar(50) not null,
    preco_unitario float not null,
    qtd int not null,
    primary key (id_produto)
);

create table cliente (
    id_cliente int,
    nome varchar(50),
    cpf varchar(11) not null,
    primary key (id_cliente)
);

create table compras (
    id_compra int,
    id_cliente int,
    id_produto int,
    data_venda date not null,
    qtd_venda int not null,
    primary key (id_cliente, id_compra, id_produto),
    foreign key (id_produto) references produto (id_produto),
    foreign key (id_cliente) references cliente (id_cliente)
)