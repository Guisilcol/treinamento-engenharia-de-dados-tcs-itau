### **Atividade 1: Criação de Tabelas Externas no AWS Glue**

**Objetivo:** Ensinar como criar tabelas externas no Glue Catalog para organizar dados armazenados no S3.

#### **Descrição:**
Criar uma tabela externa no Glue Catalog que referencia arquivos em um bucket S3. Essa tabela será usada para leitura e transformação de dados em um Glue Job.

#### **Tarefas:**
1. Crie uma base de dados no Glue Catalog.
2. No console do Glue, adicione uma tabela externa com as seguintes propriedades:
   - **Localização no S3:** `s3://meu-bucket/sor/transacoes/`
   - **Formato dos dados:** CSV
   - **Esquema:**  
     - `id_transacao` (string)  
     - `id_cliente` (string)  
     - `valor` (double)  
     - `data_transacao` (string)  
     - `categoria` (string)
3. Teste a tabela utilizando **Athena** para garantir que os dados podem ser consultados.

#### **Resultado Esperado:**  
Uma tabela no Glue Catalog que permite consultar os dados do bucket S3.

---

### **Atividade 2: Criação de um Glue Job**

**Objetivo:** Praticar a criação de um Glue Job para transformar dados catalogados no Glue Catalog.

#### **Descrição:**
Crie um Glue Job que leia os dados da tabela externa e aplique as seguintes transformações:
1. Filtrar transações com valor maior que R$ 1000.
2. Adicionar uma coluna calculada `valor_em_dolar`, que converte o valor para dólares (suponha uma taxa fixa de 5,00).
3. Gravar os dados transformados no bucket `s3://meu-bucket/sot/transacoes_filtradas/` no formato Parquet.

#### **Tarefas:**
1. Crie um Glue Job no console.
2. Implemente a lógica de transformação no script do Job.
3. Execute o Job e valide os dados no bucket S3 de destino.

---

### **Atividade 3: Orquestração com AWS Step Functions**

**Objetivo:** Criar um workflow no Step Functions que orquestre o processo completo de ETL.

#### **Descrição:**
Você criará um workflow que realiza as seguintes etapas:
1. Executar o **Glue Crawler** para catalogar dados no Glue Catalog.
2. Rodar o **Glue Job** criado anteriormente para transformar os dados.
3. Enviar uma notificação com o status do pipeline usando uma função Lambda.

#### **Tarefas:**
1. Acesse o console do Step Functions e crie uma State Machine com os seguintes estados:
   - **Executar Crawler:**  
     - Chama o Glue Crawler.
   - **Executar Glue Job:**  
     - Executa o Job de ETL criado na Atividade 2.
   - **Enviar Notificação:**  
     - Usa uma Lambda para notificar via SNS o sucesso ou falha.
2. Use o seguinte JSON como modelo para o workflow:

```json
{
  "StartAt": "Executar Crawler",
  "States": {
    "Executar Crawler": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startCrawler",
      "Parameters": {
        "Name": "meu-crawler"
      },
      "Next": "Executar Glue Job"
    },
    "Executar Glue Job": {
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun.sync",
      "Parameters": {
        "JobName": "meu-job-glue"
      },
      "Next": "Enviar Notificação"
    },
    "Enviar Notificação": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:enviarNotificacao",
      "End": true
    }
  }
}
```

3. Teste o workflow e capture logs de execução no CloudWatch.

---

### **Atividade 4: Integração com Lambda para Disparar Step Functions**

**Objetivo:** Configurar uma função Lambda para iniciar o workflow no Step Functions automaticamente quando um arquivo for enviado ao bucket S3.

#### **Descrição:**
Quando um arquivo CSV for enviado ao bucket `s3://meu-bucket/raw/`, a função Lambda será disparada para iniciar o Step Functions, automatizando o processo de ETL.

#### **Tarefas:**
1. Crie uma função Lambda com o código abaixo:
```python
import boto3

step_functions_client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    # Capturar o nome do arquivo enviado ao bucket
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Parâmetros do Step Functions
    input_data = {
        "bucket": bucket,
        "key": key
    }
    
    # Iniciar Step Functions
    response = step_functions_client.start_execution(
        stateMachineArn='arn:aws:states:REGION:ACCOUNT_ID:stateMachine:meu-step-function',
        input=json.dumps(input_data)
    )
    
    return {"status": "Step Function iniciado", "response": response}
```
2. Configure um gatilho S3 para a Lambda:
   - Evento: `PUT` (arquivo adicionado).
   - Bucket: `meu-bucket/raw`.

3. Teste o fluxo:
   - Envie um arquivo CSV para o bucket S3.
   - Valide se o Step Functions foi iniciado automaticamente.

---

### **Resultado Esperado**

1. **Atividade 1:** Uma tabela externa criada no Glue Catalog.  
2. **Atividade 2:** Dados transformados disponíveis no bucket `curated` em formato Parquet.  
3. **Atividade 3:** Um workflow funcional no Step Functions, automatizando o pipeline de ETL.  
4. **Atividade 4:** Um fluxo automatizado, onde a chegada de arquivos no bucket S3 inicia o pipeline completo.  
