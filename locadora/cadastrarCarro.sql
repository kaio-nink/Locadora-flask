delimiter ;;
create procedure cadastrarCarro(in tipo varchar(15), in modelo varchar(15), in marca varchar(10), in ano varchar(4), in disponivel boolean)
    begin
        insert into carro(tipo, modelo, marca, ano, disponivel) values(tipo, modelo, marca, ano, disponivel);
    end;;