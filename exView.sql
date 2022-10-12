create view relatorio_vendas (nome, id_prod,  tot_vendas) as 
(
    select p.nome, p.id_produto, sum(preco_unitario * qtd_venda)
    from produto as p natural join compras as c
    group by p.nome, p.id_produto
);