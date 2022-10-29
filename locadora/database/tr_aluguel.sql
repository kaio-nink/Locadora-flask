delimiter ;;
create trigger tr_aluguel before insert on aluguel
for each row
    begin
        declare disp boolean;

        select disponivel into disp
          from carro
          where id_carro = new.id_carro;
        
        if disp = true then
            update carro
            set disponivel = false
            where id_carro = new.id_carro;
        else
            signal SQLSTATE "45000";
        end if;

    end;;

delimiter ;
