create procedure addVenda(in id_compra int, in id_cliente int, in id_prod int, in data_venda date, in qtd_venda int)
    begin
        update produto set qtd = qtd - qtd_venda where id_produto = id_prod;
        insert into compras values(id_compra, id_cliente, id_prod, data_venda, qtd_venda);     
    end$$