### **Atividade: Construindo e Explorando uma One Big Table (OBT)**

#### **Objetivo**
Aprender a criar, organizar e consultar uma **One Big Table (OBT)** utilizando dados simulados de vendas. Serão consolidados dados de clientes, produtos e transações em uma única tabela, garantindo simplicidade e eficiência para análises.

---

#### **Cenário**

Você é responsável por construir uma OBT para o time de **vendas**. Os dados são provenientes de três tabelas separadas:
1. **Clientes**: Contém informações dos clientes, como nome e localização.
2. **Produtos**: Detalha produtos vendidos, como nome e categoria.
3. **Transações**: Registra as vendas realizadas, incluindo valores e datas.

O objetivo é consolidar essas informações em uma única tabela OBT e realizar análises como:
- Identificar os produtos mais vendidos.
- Analisar o volume de vendas por categoria e por localização do cliente.
- Estudar o comportamento de vendas em diferentes períodos.

Antes de começar a codificar, comece modelando a OBT. Pense nas colunas necessárias e como elas se relacionam entre si. Considere também a melhor forma de armazenar e organizar os dados para facilitar futuras consultas. Leia as consultas propostas e planeje a estrutura da OBT de acordo com as necessidades.

---

#### **Atividades**

##### **Parte 1: Preparação dos Dados**
1. **Crie três tabelas no formato CSV**:  
   Utilize os dados fornecidos abaixo para simular as tabelas originais.

**Tabela Clientes (`clientes.csv`):**
| id_cliente | nome       | cidade         |
|------------|------------|----------------|
| 1          | João Silva | São Paulo      |
| 2          | Maria Lima | Rio de Janeiro |
| 3          | Ana Costa  | Belo Horizonte |

**Tabela Produtos (`produtos.csv`):**
| id_produto | nome_produto  | categoria       | preco  |
|------------|---------------|-----------------|--------|
| 101        | Notebook      | Eletrônicos     | 3000.0 |
| 102        | Geladeira     | Eletrodomésticos| 1500.0 |
| 103        | Smartphone    | Eletrônicos     | 2000.0 |

**Tabela Transações (`transacoes.csv`):**
| id_transacao | id_cliente | id_produto | data       | quantidade | valor_total |
|--------------|------------|------------|------------|------------|-------------|
| 1001         | 1          | 101        | 2023-11-01 | 1          | 3000.0      |
| 1002         | 2          | 102        | 2023-11-02 | 1          | 1500.0      |
| 1003         | 3          | 103        | 2023-11-03 | 2          | 4000.0      |

---

##### **Parte 2: Consolidação em uma One Big Table**

1. **Crie uma OBT usando PySpark**:  
   - Leia os arquivos CSV usando PySpark.
   - Realize os joins necessários para consolidar as tabelas em uma única OBT.


**Exemplo de OBT resultante:**
| **id_transacao** | **data**      | **nome**       | **cidade**         | **nome_produto** | **categoria**      | **quantidade** | **valor_total** |
|-------------------|---------------|----------------|---------------------|------------------|--------------------|----------------|-----------------|
| 1001             | 2023-11-01   | João Silva     | São Paulo          | Notebook         | Eletrônicos        | 1              | 3000.0          |
| 1002             | 2023-11-02   | Maria Lima     | Rio de Janeiro     | Geladeira        | Eletrodomésticos   | 1              | 1500.0          |
| 1003             | 2023-11-03   | Ana Costa      | Belo Horizonte     | Smartphone       | Eletrônicos        | 2              | 4000.0          |

---

##### **Parte 3: Exploração e Análise**

Utilizando Python ou SQL, responda às seguintes consultas na OBT criada:

1. **Consulta 1: Produtos mais vendidos**
   - Realize uma agregação para calcular o total de vendas (`quantidade`) por produto.
   - Ordene o resultado de forma decrescente.

2. **Consulta 2: Volume de vendas por categoria**
   - Calcule o valor total de vendas (`valor_total`) por categoria.

3. **Consulta 3: Análise por localização**
   - Analise o volume de vendas (`valor_total`) por cidade.