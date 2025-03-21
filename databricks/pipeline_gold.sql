-- Compactar arquivos pequenos para melhorar a performance
OPTIMIZE delta.`/mnt/datalake/silver/transacoes`
ZORDER BY (customer_id);

-- Criar Bloom Filter para acelerar filtros em customer_id
ALTER TABLE delta.`/mnt/datalake/silver/transacoes`
ADD CONSTRAINT bloomfilter_customer_id
USING BLOOMFILTER ON (customer_id);

-- Criar tabela agregada na camada Gold (exemplo: média de gastos por ano)
CREATE TABLE delta.`/mnt/datalake/gold/transacoes_agg` AS
SELECT ano, mes, customer_id, AVG(valor_transacao) as avg_gasto
FROM delta.`/mnt/datalake/silver/transacoes`
GROUP BY ano, mes, customer_id;
