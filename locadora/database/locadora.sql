CREATE DATABASE IF NOT EXISTS Locadora;
USE Locadora;

CREATE TABLE IF NOT EXISTS cliente
(
    id_cliente INT AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    telefone VARCHAR(11),
    PRIMARY KEY(id_cliente)
);

CREATE TABLE IF NOT EXISTS carro
(
    id_carro INT AUTO_INCREMENT,
    disponivel Boolean NOT NULL,
    PRIMARY KEY (id_carro)
);

CREATE TABLE IF NOT EXISTS tipo_carro
(
    id_carro INT,
    modelo VARCHAR(10),
    marca VARCHAR(10),
    ano VARCHAR(4),
    valorDiaria NUMERIC(4,2),
    PRIMARY KEY(id_carro, modelo),
    FOREIGN KEY(id_carro) REFERENCES carro(id_carro)
);

CREATE TABLE IF NOT EXISTS aluguel
(
    id_cliente INT,
    id_carro INT,
    dataInicial DATE,
    PRIMARY KEY(id_cliente, id_carro, dataInicial),
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY(id_carro) REFERENCES carro(id_carro)
);