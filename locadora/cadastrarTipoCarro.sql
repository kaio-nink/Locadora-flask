delimiter ;;
create procedure cadastrarTipoCarro(in tipo varchar(15), in valorDiaria numeric(4,2), in valorSemanal numeric(7,2))
    begin
        insert into tipo_carro(tipo, valorDiaria, valorSemanal) values(tipo, valorDiaria, valorSemanal);
    end;;