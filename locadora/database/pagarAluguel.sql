delimiter ;;
CREATE PROCEDURE pagarAluguel(in id_cliente INT, in id_veiculo INT, IN dataInicial DATE)
  BEGIN
      UPDATE Aluguel AS A
        SET pendente = FALSE
        WHERE A.id_cliente = id_cliente AND A.id_veiculo = id_veiculo AND A.dataInicial = dataInicial;
  END;;

DELIMITER ;