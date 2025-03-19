## **O que são Window Functions?**
Uma **Window Function** permite que você realize cálculos sobre um subconjunto de dados sem agrupá-los, o que significa que os valores calculados ainda são exibidos **ao lado dos dados originais**.

### **Sintaxe básica de uma Window Function**
```sql
SELECT coluna1, coluna2, 
       função_de_janela() OVER (PARTITION BY coluna ORDER BY coluna) AS resultado
FROM tabela;
```
**Componentes principais**:
- `função_de_janela()`: Qualquer função agregada (como `SUM`, `AVG`, `ROW_NUMBER`, etc.).
- `OVER()`: Define a **janela (window)** sobre a qual a função será aplicada.
- `PARTITION BY`: (Opcional) Divide os dados em grupos antes de aplicar a função.
- `ORDER BY`: (Opcional) Define a ordem dentro de cada partição.

---

## **Exemplo 1: Calculando a média móvel de vendas**
Imagine que temos uma tabela de vendas (`Vendas`) e queremos calcular a **média móvel de vendas dos últimos três meses** para cada produto.

### **Tabela Vendas**
| ID_Venda | Produto  | Data_Venda | Valor |
|----------|---------|------------|-------|
| 1        | A       | 2024-01-10 | 100   |
| 2        | A       | 2024-02-10 | 200   |
| 3        | A       | 2024-03-10 | 150   |
| 4        | A       | 2024-04-10 | 250   |
| 5        | A       | 2024-05-10 | 300   |

### **Consulta usando Window Function**
```sql
SELECT Produto, Data_Venda, Valor,
       AVG(Valor) OVER (PARTITION BY Produto ORDER BY Data_Venda ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS Media_Movel
FROM Vendas;
```
### **Explicação**
1. A função `AVG(Valor)` calcula a média de vendas.
2. `PARTITION BY Produto` faz com que o cálculo seja separado por produto.
3. `ORDER BY Data_Venda` ordena as vendas cronologicamente.
4. `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` define que a média deve ser calculada considerando a linha atual e as duas anteriores.

---

## **Exemplo 2: Ranking de funcionários por salário**
Imagine que você tem uma tabela de funcionários e deseja classificar os funcionários dentro de cada departamento **com base no salário**.

### **Tabela Funcionarios**
| ID | Nome   | Departamento | Salario |
|----|--------|-------------|---------|
| 1  | Ana    | Vendas      | 7000    |
| 2  | Bruno  | TI          | 6000    |
| 3  | Carla  | Vendas      | 5000    |
| 4  | Daniel | Vendas      | 8000    |
| 5  | Erika  | TI          | 5500    |

### **Consulta usando Window Function**
```sql
SELECT Nome, Departamento, Salario,
       RANK() OVER (PARTITION BY Departamento ORDER BY Salario DESC) AS Ranking
FROM Funcionarios;
```
### **Explicação**
1. A função `RANK()` atribui uma posição para cada funcionário dentro do seu departamento.
2. `PARTITION BY Departamento` cria rankings separados por departamento.
3. `ORDER BY Salario DESC` ordena os salários de forma decrescente.

Resultado esperado:

| Nome   | Departamento | Salario | Ranking |
|--------|-------------|---------|---------|
| Daniel | Vendas      | 8000    | 1       |
| Ana    | Vendas      | 7000    | 2       |
| Carla  | Vendas      | 5000    | 3       |
| Bruno  | TI          | 6000    | 1       |
| Erika  | TI          | 5500    | 2       |

---

## **Exemplo 3: Reescrevendo uma consulta complexa com subconsultas**
Sem usar Window Functions, encontrar o **segundo maior salário por departamento** pode ser uma consulta complicada.

### **Consulta original sem Window Functions**
```sql
SELECT Nome, Departamento, Salario FROM Funcionarios f1
WHERE 2 = (
    SELECT COUNT(DISTINCT Salario)
    FROM Funcionarios f2
    WHERE f1.Departamento = f2.Departamento
    AND f2.Salario >= f1.Salario
);
```
### **Problemas dessa consulta**
- Usa subconsultas aninhadas que dificultam a leitura.
- Pode ter problemas de desempenho em tabelas grandes.
- Difícil de entender e modificar.

### **Consulta reescrita usando Window Function**
```sql
WITH RankingSalarios AS (
    SELECT Nome, Departamento, Salario,
           DENSE_RANK() OVER (PARTITION BY Departamento ORDER BY Salario DESC) AS Ranking
    FROM Funcionarios
)
SELECT Nome, Departamento, Salario
FROM RankingSalarios
WHERE Ranking = 2;
```
### **Explicação**
1. A CTE `RankingSalarios` calcula um ranking de salários por departamento.
2. A função `DENSE_RANK()` gera um ranking sem pular posições (diferente de `RANK()`).
3. A consulta final filtra apenas os funcionários com o **segundo maior salário** (`WHERE Ranking = 2`).

Resultado esperado:

| Nome  | Departamento | Salario |
|-------|-------------|---------|
| Ana   | Vendas      | 7000    |
| Erika | TI          | 5500    |

Isso simplifica bastante a consulta original e melhora a **legibilidade e desempenho**.

---

## **Vantagens do Uso de Window Functions**
- **Mantém todas as linhas da consulta** – Diferente de funções agregadas (`SUM`, `AVG`), que reduzem o número de linhas.
- **Facilita cálculos complexos** – Como médias móveis, rankings e percentuais.
- **Melhora a performance** – Evita subconsultas aninhadas desnecessárias.
- **Código mais legível e modular** – Mais fácil de entender e modificar.

---

## **Recomendação de vídeos**
Para aprofundar ainda mais o conhecimento sobre **Window Functions no SQL**, recomendo assistir ao seguinte vídeo:

🔗 **[Windows Functions - o que são e como funcionam?](https://www.youtube.com/watch?v=MzxIhnIaXuY)**