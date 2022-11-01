delimiter ;;
create procedure cadastrarAluguel(in id_cliente int, in id_veiculo int, in dataInicial date, in numDias int)
    begin
        insert into Aluguel(id_cliente, id_veiculo, dataInicial, numDias) values(id_cliente, id_veiculo, dataInicial, numDias);
    end;;