create procedure addProduto(in id_produto int, in nome varchar(50), in preco_unitario float, in qtd int)
    begin
        insert into produto values(id_produto, nome, preco_unitario, qtd);
    end$$