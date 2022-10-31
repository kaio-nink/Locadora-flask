delimiter ;;
create procedure cadastrarCliente(in nome varchar(30), in telefone varchar(12))
    begin
        insert into Cliente(nome, telefone) values(nome, telefone);
    end;;