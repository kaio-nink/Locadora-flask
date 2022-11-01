delimiter ;;
create procedure cadastrarCategoria(in categoria varchar(15), in valorDiaria numeric(5,2), in valorSemanal numeric(10,2))
    begin
        insert into Categoria_veiculo(categoria, valorDiaria, valorSemanal) 
          values(categoria, valorDiaria, valorSemanal);
    end;;
delimiter ;