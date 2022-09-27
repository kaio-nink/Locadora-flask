create procedure tot_venda(in id_prod int, out total_vendas int)
    begin
        select sum(qtd_venda) into total_vendas
        from compras
        where id_produto = id_prod;
    end$$
    