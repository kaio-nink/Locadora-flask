CREATE VIEW relatorioVeiculo(id_veiculo, veiculo, categoria) AS (
  SELECT id_carro AS id_veiculo, concat(marca , " " , modelo, " " , ano) AS veiculo, tipo AS categoria
    FROM carro
);