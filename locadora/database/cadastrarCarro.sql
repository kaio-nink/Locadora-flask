delimiter ;;
create procedure cadastrarVeiculo(in marca varchar(10), in modelo varchar(15), in categoria varchar(15), in ano varchar(4))
    begin
        insert into Veiculo(marca, modelo, categoria, ano) values(marca, modelo, categoria, ano);
    end;;