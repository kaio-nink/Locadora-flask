delimiter ;;
create procedure cadastrarAluguel(in id_cliente int, in id_carro int, in dataInicial date, in numDias int)
    begin
        insert into aluguel(id_cliente, id_carro, dataInicial, numDias) values(id_cliente, id_carro, dataInicial, numDias);
    end;;