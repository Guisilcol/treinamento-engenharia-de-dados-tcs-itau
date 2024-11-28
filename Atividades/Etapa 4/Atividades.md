### Atividades para a Etapa: DataFrames e Manipulação de Dados em Spark

#### **1. Atividade 1: Carregamento de Dados e Operações Básicas**

**Objetivo:** Ensinar como carregar dados em um DataFrame e realizar operações básicas como seleção de colunas, filtragem e contagem.

**Descrição:**  
O participante deve carregar um arquivo CSV contendo informações fictícias de clientes e realizar operações simples.

**Tarefas:**
1. Carregar um arquivo CSV em um DataFrame.
2. Selecionar as colunas `nome`, `idade` e `cidade`.
3. Filtrar os clientes com idade maior que 30.
4. Contar quantos clientes são da cidade de "São Paulo".

**Dados necessários:**  
Arquivo: **clientes.csv**

| id_cliente | nome      | idade | cidade         |
|------------|-----------|-------|----------------|
| 1          | João      | 35    | São Paulo      |
| 2          | Maria     | 25    | Rio de Janeiro |
| 3          | José      | 40    | Curitiba       |
| 4          | Ana       | 28    | São Paulo      |
| 5          | Paulo     | 50    | Belo Horizonte |

---

#### **2. Atividade 2: Operações Avançadas com DataFrames**

**Objetivo:** Ensinar como realizar transformações e agregações em DataFrames.

**Descrição:**  
O participante deve trabalhar com um dataset de transações financeiras, aplicando transformações e agregações para obter insights.

**Tarefas:**
1. Carregar o arquivo CSV de transações em um DataFrame.
2. Criar uma nova coluna `ano_transacao` extraindo o ano da coluna `data_transacao`.
3. Agrupar as transações por `categoria` e calcular o valor total (`valor_total`) e a média de valores (`valor_medio`).
4. Ordenar o resultado pelo `valor_total` em ordem decrescente.

**Dados necessários:**  
Arquivo: **transacoes.csv**

| id_transacao | id_cliente | valor | data_transacao | categoria      |
|--------------|------------|-------|----------------|----------------|
| 1            | 1          | 100.0 | 2023-11-01     | Compras        |
| 2            | 2          | 200.0 | 2023-11-02     | Alimentação    |
| 3            | 3          | 150.0 | 2023-11-03     | Compras        |
| 4            | 4          | 300.0 | 2023-11-01     | Viagem         |
| 5            | 5          | 50.0  | 2023-11-04     | Alimentação    |

---

#### **3. Atividade 3: Integração com Diferentes Fontes de Dados**

**Objetivo:** Demonstrar como integrar diferentes fontes de dados em um único DataFrame.

**Descrição:**  
O participante trabalhará com dois datasets: um contendo informações de clientes e outro contendo transações. O objetivo é realizar um `join` entre os dois para analisar o volume total de transações por cliente.

**Tarefas:**
1. Carregar os arquivos CSV de clientes e transações.
2. Realizar um `join` entre os dois DataFrames usando a chave `id_cliente`.
3. Criar uma nova coluna `total_transacoes` que represente o valor total de transações por cliente.
4. Identificar o cliente com o maior volume de transações.

**Dados necessários:**  
Arquivo: **clientes.csv** (igual ao da Atividade 1)  
Arquivo: **transacoes.csv** (igual ao da Atividade 2)

---

#### **4. Atividade 4: Comparação entre Pandas e PySpark**

**Objetivo:** Comparar as operações em Pandas e PySpark para entender as diferenças e similaridades entre ambas as APIs.

**Descrição:**  
Os participantes devem realizar as mesmas operações com os datasets usando Pandas e PySpark, comparando o desempenho e os resultados.

**Tarefas:**
1. Com os mesmos arquivos das atividades anteriores, realizar as seguintes operações:
   - Filtrar os clientes com idade maior que 30.
   - Agrupar as transações por `categoria` e calcular o valor total.
2. Comparar o tempo de execução e identificar as diferenças de sintaxe entre Pandas e PySpark.
