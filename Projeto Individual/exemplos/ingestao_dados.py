import os
import sqlite3
from pyspark.sql import SparkSession

DB_FILEPATH = './banco_origem.db'

# Deleta o banco de dados caso exista
if os.path.exists(DB_FILEPATH):
    os.remove(DB_FILEPATH)

# Cria uma conexão com o banco de dados SQLite (em memória)
conn = sqlite3.connect(DB_FILEPATH)

# Cria uma tabela de exemplo

conn.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Insere alguns dados de exemplo
conn.execute("INSERT INTO pessoas (nome, idade) VALUES ('Guilherme', 10)")
conn.execute("INSERT INTO pessoas (nome, idade) VALUES ('Alice', 17)")
conn.execute("INSERT INTO pessoas (nome, idade) VALUES ('Bob', 25)")
conn.execute("INSERT INTO pessoas (nome, idade) VALUES ('Charlie', 35)")
conn.execute("INSERT INTO pessoas (nome, idade) VALUES ('David', 28)")
conn.commit()
conn.close()

# Cria uma sessão do PySpark
spark: SparkSession = (
    SparkSession
    .builder
    .enableHiveSupport() # type: ignore
    .config('spark.jars.packages', 'org.xerial:sqlite-jdbc:3.34.0') # type: ignore
    .master('local[*]')
    .getOrCreate()
)

# Le os dados da tabela "pessoas" e cria um DataFrame do PySpark
df = (
    spark.read
    .format('jdbc')
    .option('url', f'jdbc:sqlite:{DB_FILEPATH}')
    .option('driver', 'org.sqlite.JDBC')
    #.option('dbtable', 'pessoas') # Lê a tabela inteira
    .option('query', 'SELECT * FROM pessoas') # Retorna o resultado da consulta SQL
    .load()
)

# Crio minha tabela de ingestao caso nao exista 
spark.sql("""
CREATE EXTERNAL TABLE IF NOT EXISTS ingestao_pessoas (
    id INTEGER,
    nome STRING,
    idade INTEGER
)
STORED AS PARQUET
LOCATION './tmp/ingestao_pessoas'
""")

# Carrega os dados da tabela "pessoas" em uma tabela do catalogo 
df.write.insertInto('ingestao_pessoas', overwrite=True)

# Deleta o banco de dados SQLite
os.remove(DB_FILEPATH)