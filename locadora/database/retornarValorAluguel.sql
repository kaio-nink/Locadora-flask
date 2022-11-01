delimiter ;;
CREATE FUNCTION valorAluguel(categoria varchar(15), numDias int) RETURNS FLOAT READS SQL DATA
  BEGIN
    DECLARE vDiaria DECIMAL(5,2);
    DECLARE vSemanal DECIMAL(7,2);
    DECLARE valorTotal FLOAT;
    DECLARE numSemanas INT;

    SELECT valorDiaria, valorSemanal INTO vDiaria, vSemanal
      FROM Categoria_veiculo AS C
      WHERE C.categoria = categoria;


    SET numSemanas = FLOOR(numDias/7);
    SET numDias = MOD(numDias, 7);
    
    SET valorTotal = (vSemanal * numSemanas) + (vDiaria * numDias);

    RETURN valorTotal;

  END;;
DELIMITER ;
