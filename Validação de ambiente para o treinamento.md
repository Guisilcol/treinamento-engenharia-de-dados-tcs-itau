
# Tutorial de Validação do Ambiente para Treinamento

Este tutorial orienta o aluno na instalação e validação dos componentes necessários para o treinamento, abrangendo a instalação do Java, Apache Spark (incluindo a configuração para o Spark Connect com winutils no Windows) e Python + PySpark.

---

## 1. Instalação do Java

O Apache Spark depende do Java (JDK) para funcionar. Recomenda-se o uso do JDK 11 ou superior.

### 1.1. Windows

1. **Download do JDK:**  
   Acesse o site oficial do [Adoptium](https://adoptium.net) ou da [Oracle](https://www.oracle.com/java/technologies/downloads/) e baixe a versão adequada do JDK (preferencialmente JDK 11).

2. **Instalação:**  
   Execute o instalador e siga as instruções.

3. **Configuração da variável JAVA_HOME:**  
   - Clique com o botão direito em "Este Computador" e selecione **Propriedades**.  
   - Vá em **Configurações Avançadas do Sistema** > **Variáveis de Ambiente**.  
   - Crie ou edite a variável `JAVA_HOME` apontando para o diretório de instalação do JDK (por exemplo, `C:\Program Files\Java\jdk-11.0.x`).  
   - Adicione `%JAVA_HOME%\bin` à variável `PATH`.

4. **Validação:**  
   Abra o **Prompt de Comando** e execute:
   ```bash
   java -version
   ```
   Verifique se a versão exibida corresponde à instalada.

### 1.2. Linux (Debian/Ubuntu)

1. Atualize a lista de pacotes:
   ```bash
   sudo apt update
   ```

2. Instale o OpenJDK 11:
   ```bash
   sudo apt install openjdk-11-jdk
   ```

3. Valide a instalação:
   ```bash
   java -version
   ```

---

## 2. Instalação do Apache Spark

Utilize a versão pré-compilada do Spark para facilitar a instalação. Recomenda-se uma versão compatível com Hadoop 3.3, que também assegura o suporte ao Spark Connect.

### 2.1. Download e Extração

1. Acesse a página oficial do [Apache Spark](https://spark.apache.org/downloads.html).  
2. Selecione a versão pré-compilada para **Hadoop 3.3**.  
3. Faça o download do arquivo compactado e extraia-o para um diretório, por exemplo:

   - **Windows:** `C:\spark`
   - **Linux:** `/opt/spark`

### 2.2. Configuração

#### Windows

1. **Variáveis de Ambiente:**  
   - Configure a variável `SPARK_HOME` apontando para o diretório onde o Spark foi extraído (ex.: `C:\spark`).  
   - Adicione `%SPARK_HOME%\bin` à variável `PATH`.

2. **Integração do winutils.exe:**  
   O Spark no Windows pode depender do `winutils.exe` para executar certas funcionalidades relacionadas ao Hadoop. Para Spark pré-compilado para Hadoop 3.3, baixe o winutils compatível:
   - **Link para download:** [winutils para Hadoop 3.3](https://github.com/kontext-tech/winutils/tree/master/hadoop-3.3.1/bin) ou [link direto](blob:https://github.com/ace6b6f0-e318-4150-bd58-572f4b35cf0f)
   - Baixe o `winutils.exe` e coloque-o em um diretório, por exemplo: `C:\hadoop\bin`.
   - Configure a variável de ambiente `HADOOP_HOME` para o diretório raiz (ex.: `C:\hadoop`) e adicione `%HADOOP_HOME%\bin` ao `PATH`.

#### Linux

1. Extraia o arquivo para o diretório desejado:
   ```bash
   sudo mkdir -p /opt/spark
   sudo tar -xzf spark-*.tgz -C /opt/spark --strip-components=1
   ```
2. Configure a variável `SPARK_HOME` adicionando as seguintes linhas ao arquivo `~/.bashrc` (ou equivalente):
   ```bash
   export SPARK_HOME=/opt/spark
   export PATH=$SPARK_HOME/bin:$PATH
   ```
3. Aplique as mudanças:
   ```bash
   source ~/.bashrc
   ```

### 2.3. Validação do Spark

Abra o **Prompt de Comando** (Windows) ou o **Terminal** (Linux) e execute:
```bash
spark-submit --version
```
ou
```bash
spark-shell
```
para confirmar que o Spark foi instalado corretamente.

---

## 3. Instalação do Python e PySpark

### 3.1. Instalação do Python

#### Windows

1. Baixe o instalador do [Python](https://www.python.org/downloads/) e execute-o.
2. Durante a instalação, marque a opção **"Add Python to PATH"**.
3. Verifique a instalação abrindo o **Prompt de Comando** e digitando:
   ```bash
   python --version
   ```

#### Linux

Caso o Python não esteja instalado, use (para distribuições baseadas em Debian):
```bash
sudo apt install python3 python3-pip
```

### 3.2. Instalação do PySpark e Início do Python

1. **Instalação do PySpark:**  
   Abra o **Prompt de Comando** (no Windows) ou o **Terminal** (no Linux) e execute o comando:
   ```bash
   pip install pyspark
   ```
   Esse comando fará o download e a instalação do PySpark e suas dependências.

2. **Como iniciar o Python para testar o PySpark:**

   - **Windows:**
     1. Abra o **Prompt de Comando** (pressione `Win + R`, digite `cmd` e pressione Enter).
     2. No prompt, digite o comando abaixo para iniciar o interpretador Python:
        ```bash
        python
        ```
     3. Dentro do interpretador Python, você verá um prompt interativo (geralmente `>>>`). Digite:
        ```python
        import pyspark
        print(pyspark.__version__)
        ```
     4. Se a versão do PySpark for exibida sem erros, a instalação está correta.
     5. Para sair do interpretador Python, digite:
        ```python
        exit()
        ```
     
   - **Linux:**
     1. Abra o **Terminal**.
     2. Digite o comando para iniciar o Python:
        ```bash
        python3
        ```
     3. No prompt interativo, digite:
        ```python
        import pyspark
        print(pyspark.__version__)
        ```
     4. Se a versão do PySpark for exibida sem erros, a instalação está correta.
     5. Para sair, digite:
        ```python
        exit()
        ```

---

## 4. Configuração do Spark Connect

O Spark Connect permite que aplicações se conectem remotamente ao cluster Spark. Para assegurar a compatibilidade:

1. **Verifique as Variáveis de Ambiente:**  
   Confirme que `JAVA_HOME`, `SPARK_HOME` e (no Windows) `HADOOP_HOME` estão configurados corretamente.

2. **Teste a Conexão via PySpark:**  
   Crie um script Python para testar a conexão com o Spark:
   ```python
   from pyspark.sql import SparkSession

   # Cria uma sessão Spark com suporte ao Spark Connect (ajuste os parâmetros conforme necessário)
   spark = SparkSession.builder \
       .appName("TesteSparkConnect") \
       .getOrCreate()

   # Exibe a versão do Spark
   print(spark.version)
   spark.stop()
   ```
   Salve esse script em um arquivo (por exemplo, `teste_spark_connect.py`), abra o terminal ou prompt de comando, navegue até o diretório onde o arquivo foi salvo e execute:
   ```bash
   python teste_spark_connect.py
   ```
   Se não ocorrerem erros e a versão do Spark for exibida, a conexão está funcionando corretamente.

---

## 5. Validação Final

Após a instalação e configuração, valide cada componente:

- **Java:**  
  No terminal/prompt:
  ```bash
  java -version
  ```

- **Apache Spark:**  
  Verifique com:
  ```bash
  spark-submit --version
  ```

- **Python e PySpark:**  
  Teste com:
  ```bash
  python -c "import pyspark; print(pyspark.__version__)"
  ```

- **Spark Connect:**  
  Execute o script de teste mencionado na seção anterior para confirmar que a conexão ao Spark está funcionando.

---

## 6. Script de Teste para Validação do Código Spark

A seguir, um script em Python que gera uma massa de dados (arquivo com no mínimo 100 MB), lê essa massa via PySpark e carrega os dados em uma tabela particionada no catálogo utilizando arquivos no formato PARQUET.

```python
# script_teste_spark.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
import random, string

def random_string(n=200):
    """Gera uma string aleatória de n caracteres."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

# Registra a UDF para gerar strings aleatórias
random_string_udf = udf(lambda: random_string(), StringType())

# Inicializa a sessão Spark
spark = SparkSession.builder \
    .appName("TesteMassaDeDados") \
    .getOrCreate()

# Gera um DataFrame com 1 milhão de linhas e uma coluna de string de 200 caracteres.
# Isso garante que o arquivo gerado seja, no mínimo, 100 MB.
df = spark.range(0, 1000000) \
    .withColumn("random_str", random_string_udf()) \
    .withColumn("partition_col", (col("id") % 10))

# Caminho de saída para salvar os dados em formato PARQUET particionado
output_path = "data_parquet"

# Salva o DataFrame como arquivos PARQUET particionados pela coluna 'partition_col'
df.write.partitionBy("partition_col").mode("overwrite").parquet(output_path)

# Cria uma base de dados e uma tabela no catálogo apontando para os arquivos gerados
spark.sql("CREATE DATABASE IF NOT EXISTS test_db")
spark.sql("USE test_db")
spark.sql("DROP TABLE IF EXISTS test_table")
spark.sql(f"CREATE TABLE test_table USING PARQUET LOCATION '{output_path}'")

print("Script executado com sucesso. Tabela 'test_table' criada no banco 'test_db'.")
spark.stop()
```

### 6.1. Como Executar o Script de Teste

1. **Certifique-se de que o ambiente está configurado conforme as seções anteriores.**
2. Salve o script acima em um arquivo chamado `script_teste_spark.py`.
3. Abra o **Prompt de Comando** (no Windows) ou o **Terminal** (no Linux).
4. Navegue até o diretório onde o arquivo `script_teste_spark.py` foi salvo.
5. Execute o script com o comando:
   ```bash
   python script_teste_spark.py
   ```
6. Após a execução, verifique se a saída indica que a tabela `test_table` foi criada no banco de dados `test_db`.
