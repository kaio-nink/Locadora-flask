create procedure addCliente(in id_cliente int, in nome varchar(50), in cpf varchar(11))
    begin
        insert into cliente values(id_cliente, nome, cpf);
    end$$