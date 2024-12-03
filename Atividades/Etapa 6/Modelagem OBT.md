# **Modelagem One Big Table (OBT)**

A modelagem **One Big Table (OBT)** é uma abordagem de design de tabelas amplamente utilizada em contextos analíticos e em arquiteturas de Data Warehouses e Data Lakes. Ela se caracteriza por consolidar dados de diferentes origens e granularidades em uma única tabela, otimizando a consulta e simplificando a interação dos analistas com os dados.

Embora apresente vantagens em cenários específicos, a OBT também tem desafios e limitações. Este documento explora o conceito, os casos de uso, as vantagens, e os cuidados a serem considerados ao adotar essa abordagem.

Essa modelagem é recomendada pelo Itaú. Sempre que possível, utilize-a para simplificar a interação dos analistas e a área de negócio.

---

## **1. O que é a Modelagem One Big Table?**

Na modelagem OBT, todos os atributos relevantes de um domínio ou processo são colocados em uma única tabela, ao invés de serem divididos em tabelas normalizadas, como acontece em modelagens relacionais tradicionais.

**Exemplo:**  
Imagine que você está lidando com dados de vendas. Em uma modelagem OBT, uma única tabela poderia conter:
- Informações sobre o cliente (nome, localização).
- Detalhes do produto (nome, categoria, preço).
- Dados da venda (data, valor total, quantidade).

Em um modelo normalizado, essas informações estariam divididas em várias tabelas, como `Clientes`, `Produtos`, `Vendas`, `ItensVenda`, como segue o exemplo:

**Tabela Clientes**
| **ID** | **Nome** | **Localização** |
|--------|----------|-----------------|
| 1      | João Silva | São Paulo |
| 2      | Maria Santos | Rio de Janeiro |

**Tabela Produtos**
| **ID** | **Nome** | **Categoria** | **Preço** |
|--------|----------|---------------|-----------|
| 1      | Notebook | Eletrônicos | 3000.00 |
| 2      | Geladeira | Eletrodomésticos | 1500.00 |

**Tabela Vendas**
| **ID** | **Data** | **ClienteID** | **Valor Total** |
|--------|----------|---------------|-----------------|
| 1      | 2023-11-01 | 1 | 3000.00 |
| 2      | 2023-11-02 | 2 | 1500.00 |

**Tabela ItensVenda**
| **VendaID** | **ProdutoID** | **Quantidade** |
|-------------|---------------|----------------|
| 1           | 1             | 1 |
| 2           | 2             | 1 |


A tabela OBT seria algo assim:

| **Data**   | **Cliente**  | **Produto** | **Categoria** | **Preço** | **Quantidade** | **Valor Total** |
|------------|--------------|-------------|---------------|-----------|----------------|-----------------|
| 2023-11-01 | João Silva   | Notebook    | Eletrônicos   | 3000.00   | 1              | 3000.00         |
| 2023-11-02 | Maria Santos | Geladeira   | Eletrodomésticos | 1500.00 | 1              | 1500.00         |

---

## **2. Características Principais**

1. **Desnormalização:**  
   Todos os dados relevantes são consolidados em uma tabela única, eliminando a necessidade de múltiplos joins.

2. **Orientação Analítica:**  
   Ideal para cenários de **BI (Business Intelligence)** e **dashboards**, onde consultas rápidas são mais importantes que a eficiência de armazenamento.

3. **Granularidade Fixa:**  
   Geralmente, a tabela é organizada em um nível específico, como transações, visitas ou eventos, dependendo do contexto.

---

## **3. Vantagens da Modelagem OBT**

1. **Simplicidade para os Usuários:**  
   - Com todos os dados em uma única tabela, os analistas não precisam conhecer relacionamentos complexos entre tabelas. Isso simplifica a criação de relatórios e dashboards.

2. **Desempenho de Consulta:**  
   - Como elimina a necessidade de joins, consultas em uma OBT geralmente têm melhor desempenho em ferramentas analíticas como Power BI, Tableau ou Athena.

3. **Facilidade de Implementação:**  
   - É mais rápido construir uma OBT consolidando dados de várias fontes do que projetar um modelo altamente normalizado.

4. **Compatibilidade com Ferramentas de BI:**  
   - Muitas ferramentas analíticas funcionam melhor com dados em formato tabular consolidado.

---

## **4. Limitações e Desafios**

1. **Redundância de Dados:**  
   - A desnormalização aumenta a duplicação de dados, o que pode levar a um maior consumo de armazenamento.

2. **Manutenção Complexa:**  
   - Alterar ou atualizar uma OBT pode ser mais trabalhoso, pois qualquer mudança exige a reconstrução ou atualização de toda a tabela.

3. **Perda de Flexibilidade:**  
   - Modelos altamente agregados e consolidados podem limitar análises mais detalhadas ou mudanças futuras nas perguntas de negócios.

4. **Escalabilidade:**  
   - À medida que os dados crescem em volume e diversidade, uma tabela OBT pode se tornar difícil de gerenciar e processar.

5. **Granularidade Fixa:**  
   - Se a granularidade for inadequada, pode ser difícil atender a diferentes requisitos analíticos.

---

## **5. Quando Utilizar a Modelagem OBT**

### **Casos de Uso Comuns**
1. **Dashboards e Relatórios Simples:**  
   - Quando o objetivo é oferecer insights rápidos e padronizados para usuários finais não técnicos.

2. **Análises Operacionais:**  
   - Para casos em que a granularidade dos dados é clara e consistente, como transações diárias.

3. **Camada de Consumo em Data Lakehouses:**  
   - A OBT pode ser utilizada na camada refinada de um Data Lakehouse, onde os dados já foram transformados e preparados para consumo.

4. **Prototipação:**  
   - Em projetos iniciais de BI, a OBT pode ser usada para acelerar a entrega de resultados.

### **Quando Evitar**
- **Cenários de Alta Variabilidade:**  
  - Se os requisitos analíticos mudam frequentemente, um modelo mais flexível pode ser necessário.
- **Dados de Alto Volume:**  
  - Quando o volume de dados ultrapassa o que pode ser gerenciado eficientemente em uma única tabela.

---

## **6. Boas Práticas para Construir uma OBT**

1. **Escolha a Granularidade Certa:**  
   - Certifique-se de que a granularidade atende às necessidades analíticas principais (ex.: nível de transação, diário, semanal).

2. **Use Particionamento:**  
   - Divida a tabela em partições baseadas em tempo ou categorias para melhorar o desempenho em consultas e facilitar a manutenção.

3. **Automatize a Atualização:**  
   - Utilize pipelines ETL para construir e atualizar a OBT automaticamente, minimizando erros manuais.

4. **Documente o Modelo:**  
   - Inclua descrições claras das colunas e da granularidade para que os usuários entendam os dados.

5. **Combine com um Modelo Normalizado:**  
   - Use a OBT como uma camada de consumo, mas mantenha um modelo normalizado como fonte para maior flexibilidade.

---

## **7. Conclusão**

A modelagem **One Big Table (OBT)** é uma abordagem poderosa em cenários analíticos, especialmente em organizações que priorizam simplicidade e desempenho para consultas. No entanto, é essencial entender seus limites e equilibrar simplicidade com flexibilidade. Ao combinar OBT com boas práticas de particionamento, automação e documentação, é possível obter os benefícios dessa abordagem enquanto mitiga seus desafios.

---