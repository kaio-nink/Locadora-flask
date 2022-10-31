CREATE VIEW relatorioAluguel(id_cliente, id_veiculo, veiculo, categoria, nome, dataInicial, numDias, dataRetorno, pendente) as
(
    select id_cliente, id_veiculo, concat(marca , " " , modelo, " " , ano) as veiculo, categoria, nome,  dataInicial, numDias, date_add(dataInicial, interval numDias day) as dataRetorno, pendente
    from Aluguel natural join Veiculo natural join Categoria_veiculo natural join Cliente
);
