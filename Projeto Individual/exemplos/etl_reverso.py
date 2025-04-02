from pyspark.sql import SparkSession

spark: SparkSession = (
    SparkSession
    .builder
    .enableHiveSupport()
    .master('local[*]')
    .getOrCreate()
)

# Le a tabela pessoas_transformada no catalogo
df = spark.read.table('pessoas_transformada')

# Filtra os dados para obter apenas as pessoas maiores de idade
df_maiores = df.filter(df.maior_idade == 1)

# Carrega os dados em um arquivo CSV 
df_maiores.toPandas().to_csv("./maiores_de_idade.csv", index=False)