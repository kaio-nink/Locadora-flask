delimiter ;;
create trigger estorno after update on compras
for each row
    begin
        update produto
        set qtd = qtd - (new.qtd_venda - old.qtd_venda)
        where id_produto = new.id_produto;
    end;;