### Estimativa de Custos para a Arquitetura AWS no Treinamento de Engenharia de Dados

Para garantir uma infraestrutura eficiente e econômica durante o treinamento de Engenharia de Dados, foi realizada uma estimativa detalhada dos custos mensais com os serviços da AWS. Confira abaixo os principais componentes e seus respectivos valores:

#### **EventBridge**
- **Uso:** 1.000 requisições por mês
- **Custo:** US$ 0,01

#### **Lambda**
- **Uso:** 2.000 requisições por mês, cada uma com 128 MB de memória RAM
- **Custo:** US$ 1,25

#### **Glue**
- **Uso:** 
  - 50 horas de execução por mês em JOBS SPARK com 2 DPUs
  - 50 horas de execução por mês em JOBS PYTHONSHELL com 1/16 DPU
- **Custo:** US$ 47,16

#### **Athena**
- **Uso:** 10.000 queries por mês, cada uma lendo 100 MB de dados
- **Custo:** US$ 8,58

#### **Step Functions**
- **Uso:** 1.000 execuções por mês, transitando por 20 estados cada
- **Custo:** US$ 0,60

#### **S3**
- **Uso:** 
  - **Armazenamento Padrão:** 100 GB
  - **Requisições PUT:** 10.000 por mês
  - **Requisições GET:** 10.000 por mês
  - **S3 Select (Dados Retornados):** 1.000 GB
- **Custo:** US$ 5,53

#### **RDS**
- **Nota:** A configuração e os custos do RDS ainda estão sendo avaliados. Será necessário consultar os arquitetos para determinar a melhor opção para esta infraestrutura.

---

### **Custo Total Mensal: US$ 63,13** *(RDS a ser revisado)*
