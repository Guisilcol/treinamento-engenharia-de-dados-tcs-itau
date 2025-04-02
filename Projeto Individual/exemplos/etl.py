from pyspark.sql import SparkSession

spark: SparkSession = (
    SparkSession
    .builder
    .enableHiveSupport()
    .master('local[*]')
    .getOrCreate()
)

# Le a tabela ingestao_pessoas no catalogo 

df = spark.read.table('ingestao_pessoas')

# Cria coluna "maior_idade" com valor 1 se idade >= 18, caso contrario 0
df = df.withColumn('maior_idade', (df.idade >= 18).cast('int'))

# Cria tabela pessoas_transformada no catalogo caso nao exista
spark.sql("""
CREATE EXTERNAL TABLE IF NOT EXISTS pessoas_transformada (
    id INTEGER,
    nome STRING,
    idade INTEGER,
    maior_idade INTEGER
)
STORED AS PARQUET
LOCATION './tmp/pessoas_transformada'
""")

# Salva o DataFrame transformado na tabela "pessoas_transformada"
df.write.mode('overwrite').insertInto('pessoas_transformada')