DELIMITER ;;
CREATE TRIGGER devolucaoVeiculo AFTER UPDATE ON Aluguel
FOR EACH ROW
    BEGIN
        DECLARE disp BOOLEAN;

        SELECT disponivel INTO disp
          FROM Veiculo
            WHERE id_veiculo = new.id_veiculo;
        IF NEW.pendente = FALSE THEN
          UPDATE Veiculo
          SET disponivel = TRUE
          WHERE id_veiculo = new.id_veiculo;
        END IF;
    END;;

DELIMITER ;
