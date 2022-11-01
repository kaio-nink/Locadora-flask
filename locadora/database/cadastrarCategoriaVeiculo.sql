delimiter ;;
create procedure cadastrarCategoriaVeiculo(in categoria varchar(15), in valorDiaria numeric(4,2), in valorSemanal numeric(7,2))
    begin
        insert into Categoria_veiculo(categoria, valorDiaria, valorSemanal) values(categoria, valorDiaria, valorSemanal);
    end;;