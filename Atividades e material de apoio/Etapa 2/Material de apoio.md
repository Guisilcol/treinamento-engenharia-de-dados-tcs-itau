# Introdução

Material de apoio para realização das tarefas de SQL.

## SELECT

**O que é:**  
A cláusula `SELECT` é usada para indicar quais colunas ou expressões queremos retornar em nossa consulta. Ela pode selecionar colunas específicas ou todas as colunas utilizando o asterisco (`*`).

**Exemplo:**  
```sql
-- Seleciona todas as colunas da tabela Clientes
SELECT * FROM Clientes;

-- Seleciona apenas as colunas nome e cidade da tabela Clientes

SELECT nome, cidade FROM Clientes;
```

---

## FROM

**O que é:**  
A cláusula `FROM` indica de qual tabela (ou tabelas) os dados serão extraídos. Ela pode ser combinada com junções (JOINs) para relacionar dados de diferentes tabelas.
Os joins precisam ter uma ou mais colunas de valores em comum para conseguir juntar os registros de uma tabela com a outra.

**Exemplo:**  
```sql
-- Seleciona os nomes dos clientes, suas cidades e o valor dos pedidos
SELECT 
    c.nome, 
    c.cidade, 
    p.valor
FROM 
    Clientes c
    JOIN Pedidos p 
        ON c.id_cliente = p.id_cliente;
```

---

## WHERE

**O que é:**  
A cláusula `WHERE` serve para filtrar os registros que atendem a determinadas condições. Ela permite especificar critérios para restringir os resultados da consulta.

**Exemplo:**  
```sql
-- Seleciona os clientes que moram em 'São Paulo'
SELECT *
FROM Clientes
WHERE cidade = 'São Paulo';
```

---

## Uso de Funções para Transformar Dados em um SELECT

**O que é:**  
SQL fornece diversas funções para transformar ou manipular os dados retornados. Entre elas, funções de agregação (como `SUM`, `AVG`, `COUNT`), funções de manipulação de strings (`UPPER`, `LOWER`, `SUBSTR`) e funções de data.

**Exemplos:**  
```sql
-- Converte o nome dos clientes para letras maiúsculas
SELECT UPPER(nome) AS nome_maiusculo, cidade
FROM Clientes;
```

---

## GROUP BY

**O que é:**  
A cláusula `GROUP BY` agrupa os registros que possuem valores iguais em determinadas colunas. É comumente utilizada junto com funções de agregação para obter resumos ou totais por grupo.

**Exemplo:**  
```sql
-- Conta quantos clientes existem por cidade
SELECT cidade, COUNT(*) AS total_clientes
FROM Clientes
GROUP BY cidade;

-- Calcula o valor total dos pedidos por cliente
SELECT id_cliente, SUM(valor) AS total_gasto
FROM Pedidos
GROUP BY id_cliente;
```

---

## HAVING

**O que é:**  
A cláusula `HAVING` é utilizada para filtrar os resultados após a aplicação do `GROUP BY`. Ela funciona de maneira similar ao `WHERE`, porém para os grupos formados.

**Exemplo:**  
```sql
-- Exibe apenas as cidades que possuem mais de 1 cliente
SELECT cidade, COUNT(*) AS total_clientes
FROM Clientes
GROUP BY cidade
HAVING COUNT(*) > 1;
```

---

## CTE (Common Table Expression)

**O que é:**  
Uma CTE é uma subconsulta nomeada definida antes da consulta principal, facilitando a organização e a legibilidade do código, especialmente em consultas complexas. Ela é iniciada pela palavra-chave `WITH`.

**Exemplo:**  
```sql
-- Cria uma CTE para calcular o total gasto por cada cliente e, em seguida, seleciona os resultados
WITH TotalGasto AS (
    SELECT id_cliente, SUM(valor) AS total_gasto
    FROM Pedidos
    GROUP BY id_cliente
)
SELECT c.nome, c.cidade, t.total_gasto
FROM Clientes c
JOIN TotalGasto t ON c.id_cliente = t.id_cliente;
```

---

## WINDOW FUNCTION

**O que é:**  
Window Functions operam sobre um conjunto de linhas (denominado "janela") que está relacionado à linha atual sem precisar agregar os dados. Elas são úteis para cálculos que precisam considerar o contexto de linhas vizinhas, como rankings, somatórios cumulativos, ou comparações com registros anteriores.

**Exemplo:**  
Imagine que queremos comparar o valor de cada pedido com o valor do pedido imediatamente anterior de cada cliente. Podemos usar a função `LAG()`:

```sql
SELECT 
    id_cliente,
    id_pedido,
    data_pedido,
    valor,
    LAG(valor) OVER (PARTITION BY id_cliente ORDER BY data_pedido) AS valor_pedido_anterior
FROM Pedidos;
```

**Explicação do exemplo:**  
- **LAG(valor):** Recupera o valor da linha anterior.
- **OVER (PARTITION BY id_cliente ORDER BY data_pedido):** Define a "janela" para cada cliente, ordenando os pedidos pela data. Assim, cada linha pode comparar seu valor com o valor do pedido imediatamente anterior do mesmo cliente.
