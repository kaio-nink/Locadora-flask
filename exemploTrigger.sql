delimiter ;;
create trigger atualiza_estoque after insert on compras
for each row
    begin
        update produto 
        set qtd = qtd - new.qtd_venda 
        where id_produto = new.id_produto;
    end;;