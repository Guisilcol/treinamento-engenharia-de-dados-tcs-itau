## **O que é uma CTE?**
Uma **Common Table Expression (CTE)** é uma estrutura temporária nomeada que pode ser referenciada dentro de uma única consulta SQL. Ela funciona como uma subconsulta, mas com a vantagem de ser mais fácil de ler e reutilizar.

### **Sintaxe básica de uma CTE**
```sql
WITH NomeDaCTE AS (
    SELECT coluna1, coluna2
    FROM Tabela
    WHERE condição
)
SELECT * FROM NomeDaCTE;
```

---

## **Exemplo 1: Calculando a média salarial e filtrando funcionários**
Imagine que você tem uma tabela de funcionários (`Funcionarios`) e quer calcular os funcionários que recebem mais do que a média salarial.

### **Tabela Funcionarios**
| ID | Nome     | Cargo      | Salario |
|----|----------|-----------|---------|
| 1  | Ana      | Gerente    | 8000    |
| 2  | Carlos   | Analista   | 5000    |
| 3  | Beatriz  | Desenvolvedor | 6000 |
| 4  | Daniel   | Analista   | 5500    |

### **Consulta usando CTE**
```sql
WITH MediaSalarial AS (
    SELECT AVG(Salario) AS SalarioMedio FROM Funcionarios
)
SELECT Nome, Cargo, Salario
FROM Funcionarios
WHERE Salario > (SELECT SalarioMedio FROM MediaSalarial);
```
### **Explicação**
1. A CTE chamada `MediaSalarial` calcula a média salarial da tabela `Funcionarios`.  
2. A consulta final usa essa CTE para encontrar funcionários cujo salário está acima da média.

---

## **Exemplo 2: Reescrevendo uma consulta complexa com subconsultas**
Em muitos casos, consultas SQL podem se tornar difíceis de entender devido ao uso excessivo de subconsultas aninhadas. Vamos ver um exemplo.

### **Consulta original sem CTE**
A consulta abaixo tenta encontrar funcionários que ganham mais do que a média salarial do mesmo departamento que "Carlos". No entanto, devido ao uso de várias subconsultas, a leitura e manutenção são complicadas.

```sql
SELECT Nome, Salario
FROM Funcionarios
WHERE Salario > (
    SELECT AVG(Salario)
    FROM Funcionarios
    WHERE Departamento = (
        SELECT Departamento
        FROM Funcionarios
        WHERE Nome = 'Carlos'
    )
);
```
### **Problemas dessa consulta**
- Usa subconsultas aninhadas que dificultam a leitura.
- O valor do departamento de "Carlos" precisa ser calculado antes da média salarial.
- A cláusula `WHERE` final pode ser confusa ao interpretar o fluxo da consulta.

### **Consulta reescrita usando CTE**
```sql
WITH DepartamentoCarlos AS (
    SELECT Departamento
    FROM Funcionarios
    WHERE Nome = 'Carlos'
),
MediaSalarialDepartamento AS (
    SELECT AVG(Salario) AS SalarioMedio
    FROM Funcionarios
    WHERE Departamento = (SELECT Departamento FROM DepartamentoCarlos)
)
SELECT Nome, Salario
FROM Funcionarios
WHERE Salario > (SELECT SalarioMedio FROM MediaSalarialDepartamento);
```
### **Explicação**
1. A CTE `DepartamentoCarlos` obtém o departamento do funcionário "Carlos".
2. A CTE `MediaSalarialDepartamento` calcula a média salarial apenas para esse departamento.
3. A consulta final lista todos os funcionários que ganham acima dessa média.

Essa abordagem melhora a **legibilidade**, pois divide a consulta em partes nomeadas e fáceis de interpretar.

---

## **Vantagens do Uso de CTEs**
- **Código mais organizado** – Melhora a legibilidade e a estrutura das consultas complexas.  
- **Reutilização** – Pode ser referenciada várias vezes dentro da mesma consulta.  
- **Melhor desempenho** – Em alguns casos, pode melhorar a otimização da consulta, especialmente em bancos como PostgreSQL e SQL Server.  
- **Facilidade na manutenção** – Dividir uma consulta complexa em partes menores torna futuras alterações mais simples.

---

## **Recomendação de vídeos**
Para aprofundar ainda mais o conhecimento sobre **CTEs no SQL**, recomendo assistir ao seguinte vídeo:

🔗 **[Common Table Expressions (CTEs) - SQL para Análise de Dados](https://www.youtube.com/watch?v=vaM-fLnOOfQ)**