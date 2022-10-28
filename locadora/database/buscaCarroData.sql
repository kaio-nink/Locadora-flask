delimiter ;;
create procedure buscaCarroData(in dataIni date, in dias int, out outputTable table)
  begin
      insert into outputTable select concat(C.marca, " ", C.modelo, " ", C.ano) as veiculo, C.tipo
        from carro as C
        where id_carro not in (
          select A.id_carro 
            from aluguel as A
            where A.dataInicial = dataIni AND date_add(A.dataInicial,A.numDias) = date_add(dataIni,dias));  
  end;;