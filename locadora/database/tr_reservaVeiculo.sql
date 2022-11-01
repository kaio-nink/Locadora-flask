DELIMITER ;;
CREATE TRIGGER reservaVeiculo AFTER INSERT ON Aluguel
FOR EACH ROW
    BEGIN
        DECLARE disp BOOLEAN;

        SELECT disponivel INTO disp
          FROM Veiculo
            WHERE id_veiculo = new.id_veiculo;
        
        IF disp = true THEN
          UPDATE Veiculo
          SET disponivel = FALSE
          WHERE id_veiculo = new.id_veiculo;
        END IF;
    END;;

DELIMITER ;
