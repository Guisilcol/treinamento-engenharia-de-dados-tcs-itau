### **Introdução ao AWS Lambda**

O **AWS Lambda** é um serviço de computação serverless (sem servidor) que permite executar código em resposta a eventos, sem a necessidade de provisionar ou gerenciar servidores. Ele é altamente escalável e integrado com diversos serviços da AWS, sendo ideal para automação de tarefas e construção de aplicações rápidas e eficientes.

---

## **Como o AWS Lambda funciona?**

1. **Eventos como gatilhos:**  
   O Lambda é ativado por eventos. Exemplos:
   - Um arquivo enviado para um bucket S3.
   - Uma mensagem publicada no SNS.
   - Uma solicitação HTTP via API Gateway.
   - Um state em uma Step Function.

2. **Execução do código:**  
   Quando o evento ocorre, o Lambda executa o código fornecido (em linguagens como Python, Node.js, Java, etc.).

3. **Escopo limitado:**  
   O código executa uma única tarefa ou um pequeno conjunto de tarefas e termina. Não é usado para longas execuções. Caso venha optar por utilizar uma Lambda tenha em mente que não é recomendado para processamento de dados em larga escala. Opte por tarefas simples, como movimentação de arquivos, validações, subir um cluster EMR, etc.

---

## **Componentes-chave do AWS Lambda**

1. **Funções Lambda:**  
   - O "coração" do Lambda. Cada função contém o código e suas configurações, como memória alocada e timeout.

2. **Camadas (Layers):**  
   - Componentes reutilizáveis que você pode adicionar às funções Lambda, como bibliotecas, dependências ou utilitários.  

3. **Gatilhos:**  
   - Serviços ou eventos que disparam a execução da função. Exemplos incluem S3, DynamoDB, Step Functions, entre outros.

4. **Permissões (IAM):**  
   - A função Lambda precisa de permissões para acessar outros serviços da AWS.

---

## **Exemplo Prático: Lambda para Processar Dados no S3**

### Cenário:
Um arquivo CSV é enviado para um bucket S3. A função Lambda lê esse arquivo, processa os dados e grava um arquivo transformado em outro bucket.

### Código Exemplo:

```python
import boto3
import csv

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Captura o bucket e o arquivo do evento
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Faz download do arquivo
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    lines = response['Body'].read().decode('utf-8').splitlines()

    # Processa o arquivo CSV
    reader = csv.DictReader(lines)
    processed_data = []
    for row in reader:
        # Exemplo de transformação: adiciona uma coluna
        row['nova_coluna'] = int(row['idade']) * 2
        processed_data.append(row)

    # Cria um novo arquivo CSV
    output_bucket = 'meu-bucket-transformado'
    output_key = f"processed/{file_key}"
    transformed_file = "\n".join([",".join(row.values()) for row in processed_data])

    # Envia o arquivo transformado para outro bucket
    s3.put_object(Bucket=output_bucket, Key=output_key, Body=transformed_file)

    return {"status": "Processamento concluído"}
```

---

## **Quando usar AWS Lambda no contexto de ETL**

1. **Automação de tarefas:**  
   Automatizar gatilhos de pipelines ETL ao integrar serviços como S3 e Step Functions. Exemplo de uso: Função Lambda que é acionada quando um arquivo é enviado para um bucket S3 e inicia a execução de um Glue Job.

2. **Orquestração de workflows:**  
   Executar tarefas específicas em pipelines mais amplos, como notificações, validações de dados ou manipulações leves.

