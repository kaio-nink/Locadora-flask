create view relatorioAluguel(tipo, veiculo, nome, dataInicial, numDias, dataRetorno) as
(
    select tipo, concat(marca , " " , modelo, " " , ano) as veiculo, nome, dataInicial, numDias, date_add(dataInicial, interval numDias day) as dataRetorno
    from aluguel natural join carro natural join tipo_carro natural join cliente
);
