delimiter ;;
create procedure cadastrarCarro(in id_carro int, in disponivel boolean)
    begin
        insert into carro(disponivel) values(disponivel);
    end;;