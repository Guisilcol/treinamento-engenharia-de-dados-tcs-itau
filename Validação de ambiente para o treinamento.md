# Tutorial de Validação do Ambiente para Treinamento

Este tutorial orienta o aluno na instalação e validação dos componentes necessários para o treinamento, abrangendo a instalação do Java, Apache Spark (incluindo a configuração para o Spark Connect com winutils no Windows) e Python 3.11 + PySpark.

---

## 1. Instalação do Java

O Apache Spark depende do Java (JDK) para funcionar. Recomenda-se o uso do JDK 11 ou superior.

### 1.1. Windows

1. **Download do JDK 11:**  
   Baixe o JDK 11 no site oficial do [Adoptium - OpenJDK 11](https://adoptium.net/?variant=openjdk11) ou da [Oracle](https://www.oracle.com/java/technologies/downloads/). Recomenda-se o uso do Adoptium.

2. **Instalação:**  
   Execute o instalador e siga as instruções.

3. **Configuração da variável JAVA_HOME (variáveis de SISTEMA):**  
   - Clique com o botão direito em "Este Computador" e selecione **Propriedades**.  
   - Vá em **Configurações Avançadas do Sistema** > **Variáveis de Ambiente**.
   - Crie ou edite a variável `JAVA_HOME` apontando para o diretório de instalação do JDK (por exemplo, `C:\Program Files\Java\jdk-11.0.x`).  
   - Adicione `%JAVA_HOME%\bin` à variável `PATH` (variável de SISTEMA).

4. **Validação:**  
   Abra o **Prompt de Comando** e execute:
   ```bash
   java -version
   ```
   Verifique se a versão exibida corresponde à instalada.

### 1.2. Linux (Debian/Ubuntu)

1. **Download e Instalação:**  
   O JDK 11 pode ser instalado diretamente dos repositórios oficiais. Para garantir o acesso à versão mais recente do OpenJDK 11, se necessário, adicione o PPA do [Adoptium](https://adoptium.net/?variant=openjdk11):
   ```bash
   sudo apt update
   sudo apt install openjdk-11-jdk
   ```
   *Alternativamente, caso sua distribuição não possua a versão 11, considere utilizar o PPA:*
   ```bash
   sudo add-apt-repository ppa:openjdk-r/ppa
   sudo apt update
   sudo apt install openjdk-11-jdk
   ```

2. **Validação:**  
   Execute:
   ```bash
   java -version
   ```

---

## 2. Instalação do Apache Spark

Utilize a versão pré-compilada do Spark para facilitar a instalação. Recomenda-se a versão compatível com Hadoop 3.3, que também assegura o suporte ao Spark Connect.

### 2.1. Download e Extração

1. **Download:**  
   Faça o download direto do arquivo utilizando o link:  
   [https://www.apache.org/dyn/closer.lua/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz](https://www.apache.org/dyn/closer.lua/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz)

2. **Extração:**  
   Extraia o arquivo baixado para um diretório, por exemplo:
   - **Windows:** `C:\spark`
   - **Linux:** `/opt/spark`

### 2.2. Configuração

#### Windows

1. **Variáveis de Ambiente:**  
   - Configure a variável `SPARK_HOME` apontando para o diretório onde o Spark foi extraído (ex.: `C:\spark`).  
   - **Altere as variáveis de SISTEMA** para garantir que todos os usuários possam acessar a configuração.  
   - Adicione `%SPARK_HOME%\bin` à variável `PATH` (variável de SISTEMA).
   - Configure a variável `PYSPARK_PYTHON` com o valor "python"

2. **Integração do winutils.exe:**  
   O Spark no Windows depende do `winutils.exe` e `hadoop.dll` para executar funcionalidades relacionadas ao Hadoop. Para Spark pré-compilado para Hadoop 3.3, baixe o winutils compatível:
   - **Link para download:** [winutils para Hadoop 3.3](https://github.com/kontext-tech/winutils/tree/master/hadoop-3.3.1/bin)
   - Baixe o `winutils.exe` e `hadoop.dll` e os coloque em um diretório, por exemplo: `C:\hadoop\bin`.
   - Configure a variável de ambiente `HADOOP_HOME` para o diretório raiz (ex.: `C:\hadoop`) e adicione `%HADOOP_HOME%\bin` à variável `PATH` (variável de SISTEMA).

#### Linux

1. Extraia o arquivo para o diretório desejado:
   ```bash
   sudo mkdir -p /opt/spark
   sudo tar -xzf spark-3.5.5-bin-hadoop3.tgz -C /opt/spark --strip-components=1
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

## 3. Instalação do Python 3.11 e PySpark

### 3.1. Instalação do Python 3.11

#### Windows

1. **Download do Python 3.11:**  
   Baixe o instalador do [Python 3.11](https://www.python.org/downloads/release/python-3110/) e execute-o.
2. Durante a instalação, marque a opção **"Add Python to PATH"**.
3. Verifique a instalação abrindo o **Prompt de Comando** e digitando:
   ```bash
   python --version
   ```

#### Linux (Debian/Ubuntu)

Caso o Python 3.11 não esteja disponível por padrão, adicione o PPA dos deadsnakes e instale:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-dev
```
Verifique a instalação:
```bash
python3.11 --version
```

### 3.2. Instalação do PySpark e Início do Python

1. **Instalação do PySpark:**  
   Abra o **Prompt de Comando** (no Windows) ou o **Terminal** (no Linux) e execute:
   ```bash
   pip install pyspark[connect]==3.5.0
   ```
   Esse comando fará o download e a instalação do PySpark e suas dependências.

2. **Como iniciar o Python para testar o PySpark:**

   - **Windows:**
     1. Abra o **Prompt de Comando** (pressione `Win + R`, digite `cmd` e pressione Enter).
     2. No prompt, digite:
        ```bash
        python
        ```
     3. No interpretador Python (prompt `>>>`), digite:
        ```python
        import pyspark
        print(pyspark.__version__)
        ```
     4. Se a versão do PySpark for exibida sem erros, a instalação está correta.
     5. Para sair do interpretador, digite:
        ```python
        exit()
        ```
     
   - **Linux:**
     1. Abra o **Terminal**.
     2. Digite:
        ```bash
        python3.11
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
   Confirme que `JAVA_HOME`, `SPARK_HOME`, `PYSPARK_PYTHON` e (no Windows) `HADOOP_HOME` estão configurados corretamente nas variáveis de SISTEMA.

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

## 6. Inicialização do Spark Connect

### 6.1. Arquivo BAT para Windows (start_spark_connect.bat)

```bat
@echo off
REM Inicia o Spark Connect server
set CLASS="org.apache.spark.sql.connect.service.SparkConnectServer"
spark-submit --class %CLASS% --name "Spark Connect server" --packages org.apache.spark:spark-connect_2.12:3.5.5
pause
```

### 6.2. Script Shell para Linux (start_spark_connect.sh)

```bash
#!/bin/bash
# Configura a variável PYSPARK_PYTHON a nível de usuário
export PYSPARK_PYTHON=python
# Inicia o Spark Connect server
$SPARK_HOME/sbin/start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:3.5.5
```

Para finalizar o processo no Linux, utilize o seguinte script:

```bash
#!/bin/bash
$SPARK_HOME/sbin/stop-connect-server.sh
```

*Após criar o arquivo, torne-o executável (no Linux):*
```bash
chmod +x start_spark_connect.sh
```

*Para iniciar o Spark Connect, execute o arquivo correspondente:*
- **Windows:** Dê um duplo clique no `start_spark_connect.bat` ou execute-o via Prompt de Comando.
- **Linux:** Execute no terminal:
  ```bash
  ./start_spark_connect.sh
  ```

---

## 7. Script de Teste para Validação do Código Spark

A seguir, um script em Python que gera uma massa de dados (arquivo com no mínimo 100 MB), lê essa massa via PySpark e carrega os dados em uma tabela particionada no catálogo utilizando arquivos no formato PARQUET. **Atenção:** Certifique-se de que o Spark Connect server esteja iniciado (veja a seção 6) antes de executar este script.

```python
# script_teste_spark.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
import random, string

def random_string(n=200):
    """Gera uma string aleatória de n caracteres."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

# Inicializa a sessão Spark
spark = SparkSession.builder \
    .appName("TesteMassaDeDados") \
    .enableHiveSupport() \
    .master("local[*]") \
    .getOrCreate()

# Registra a UDF para gerar strings aleatórias
random_string_udf = udf(lambda: random_string(), StringType())

# Gera um DataFrame com 1 milhão de linhas e uma coluna de string de 200 caracteres.
# Isso garante que o arquivo gerado seja, no mínimo, 100 MB.
df = spark.range(0, 1000000) \
    .withColumn("random_str", random_string_udf()) \
    .withColumn("partition_col", (col("id") % 10))

# Caminho de saída para salvar os dados em formato PARQUET particionado
output_path = "./data_parquet"

# Salva o DataFrame como arquivos PARQUET particionados pela coluna 'partition_col'
df.write.partitionBy("partition_col").mode("overwrite").parquet(output_path)

# Lê os arquivos gerados e exibe as primeiras 5 linhas
spark.read.parquet(output_path).show(5)

# Cria uma base de dados e uma tabela no catálogo apontando para os arquivos gerados
df.write.saveAsTable("test_db.test_table", format="parquet", mode="overwrite", partitionBy="partition_col")
df = spark.read.table("test_db.test_table")
df.show(5)

print("Script executado com sucesso. Tabela 'test_table' criada no banco 'test_db'.")
spark.stop()
```

### 7.1. Como Executar o Script de Teste

1. **Certifique-se de que o ambiente está configurado conforme as seções anteriores e que o Spark Connect server está iniciado (veja a seção 6).**
2. Salve o script acima em um arquivo chamado `script_teste_spark.py`.
3. Abra o **Prompt de Comando** (no Windows) ou o **Terminal** (no Linux).
4. Navegue até o diretório onde o arquivo `script_teste_spark.py` foi salvo.
5. Execute o script com o comando:
   ```bash
   python script_teste_spark.py
   ```
6. Após a execução, verifique se a saída indica que a tabela `test_table` foi criada no banco de dados `test_db`.