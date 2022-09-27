create procedure get_maior_salario(out valor float)
begin
    declare maior float default 0.0;
    declare aux float;
    declare terminou boolean default false;

    declare um_cursor cursor for select preco_unitario from produto;
    declare continue handler for NOT FOUND set terminou = true;

    open um_cursor;

    while terminou <> true do
        fetch um_cursor into aux;
        if aux > maior then
            set maior = aux;
        end if;
    end while;
    close um_cursor;

    set valor = maior;
end$$
