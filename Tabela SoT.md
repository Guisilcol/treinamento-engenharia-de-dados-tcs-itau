
# Atividade: exploração em SQL para carga em tabela SoT

## Criação da tabela SoT

```sql
CREATE EXTERNAL TABLE `sot_financeira`(
  `identificador_unico` string COMMENT 'Identificador UUID do registro',
  `transacao_id` int COMMENT 'ID da transação',
  `conta_id` int COMMENT 'ID da conta',
  `categoria_id` int COMMENT 'ID da categoria',
  `transacao_data` string COMMENT 'Data da transação',
  `transacao_ano` int COMMENT 'Ano da data da transação',
  `transacao_mes` int COMMENT 'Mes da data da transação',
  `transacao_dia` int COMMENT 'Ano da data da transação',
  `transacao_descricao` string COMMENT 'Descrição da transação',
  `transacao_valor` string COMMENT 'Valor da transação',
  `transacao_data_criacao` string COMMENT 'Data de criação da transação',
  `conta_nome` string COMMENT 'Nome da conta',
  `conta_descricao` string COMMENT 'Descrição da conta',
  `categoria_nome` string COMMENT 'Nome da categoria',
  `categoria_tipo` string COMMENT 'Tipo da categoria',
  `taxa_juros_referencia` string COMMENT 'Data de referência da taxa de juros',
  `taxa_juros_porcentagem` string COMMENT 'Porcentagem da taxa de juros'
)
PARTITIONED BY ( 
  `data_ingestao` string COMMENT 'Data de ingestão dos dados'
)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://guilherme.magalhaes-sor/financeira'
TBLPROPERTIES (
  'classification'='parquet', 
  'compressionType'='snappy')
```

## Mapeamento de Campos

| Campo na OBT | Origem | Regra de Transformação |
|--------------|--------|------------------------|
| identificador_unico | N/A | Gerar um UUID v4 para cada registro (`uuid()`) |
| transacao_id | transacoes.id | Mapeamento direto |
| conta_id | transacoes.conta_id | Mapeamento direto |
| categoria_id | transacoes.categoria_id | Mapeamento direto |
| transacao_data | transacoes.data | Mapeamento direto |
| transacao_ano | transacoes.data | `EXTRACT(YEAR FROM TO_DATE(transacoes.data, 'yyyy-MM-dd'))` |
| transacao_mes | transacoes.data | `EXTRACT(MONTH FROM TO_DATE(transacoes.data, 'yyyy-MM-dd'))` |
| transacao_dia | transacoes.data | `EXTRACT(DAY FROM TO_DATE(transacoes.data, 'yyyy-MM-dd'))` |
| transacao_descricao | transacoes.descricao | Mapeamento direto |
| transacao_valor | transacoes.valor | Mapeamento direto |
| transacao_data_criacao | transacoes.data_criacao | Mapeamento direto |
| conta_nome | contas.nome | JOIN com `transacoes.conta_id = contas.id` |
| conta_descricao | contas.descricao | JOIN com `transacoes.conta_id = contas.id` |
| categoria_nome | categorias.nome | JOIN com `transacoes.categoria_id = categorias.id` |
| categoria_tipo | categorias.tipo | JOIN com `transacoes.categoria_id = categorias.id` |
| taxa_juros_referencia | interest_rate.data_referencia | Selecionar a taxa mais recente |
| taxa_juros_porcentagem | interest_rate.porcentagem | Correspondente à `taxa_juros_referencia` selecionada |
| data_processamento | transacoes.data_ingestao | Campo de particionamento mantido da tabela de origem |

