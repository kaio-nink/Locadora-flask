create function total_venda(id_prod int) returns int
    begin
        declare tot int;
        select sum(qtd_venda) into tot
        from compras
        where id_produto = id_prod;
        return tot;
    end$$