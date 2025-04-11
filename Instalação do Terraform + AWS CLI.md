# Tutorial: Instalar e Configurar Terraform e AWS CLI

## Introdução

Este tutorial tem como objetivo demonstrar como instalar e configurar o Terraform e o AWS CLI em um ambiente Windows. Com estas ferramentas, você poderá gerenciar a infraestrutura na AWS de forma automatizada e versionada.

---

## Parte 1 – Instalação e Configuração do Terraform

### 1.1 Baixando o Terraform

1. **Acesse o site oficial:**  
   Vá para a página de downloads do Terraform:  
   https://www.terraform.io/downloads.html

2. **Selecione a versão para Windows:**  
   Na seção referente ao Windows, escolha a versão adequada para a arquitetura do seu sistema (normalmente, Windows 64 bits). O download será de um arquivo compactado no formato .zip.

### 1.2 Instalando o Terraform

1. **Extraia o arquivo:**  
   Após o download, extraia o conteúdo do arquivo .zip para um diretório de sua preferência. Por exemplo, crie a pasta `C:\Terraform` e extraia o conteúdo nela.  
   O único arquivo necessário é o executável `terraform.exe`.

2. **Configuração da variável de ambiente PATH:**

   Para que o Terraform possa ser executado de qualquer prompt de comando, adicione o caminho onde o executável está localizado à variável PATH:
   - Clique com o botão direito em "Este Computador" ou "Meu Computador" e selecione **Propriedades**.
   - Selecione **Configurações Avançadas do Sistema**.
   - Clique em **Variáveis de Ambiente**.
   - Na seção **Variáveis do Sistema**, localize a variável `Path` e clique em **Editar**.
   - Clique em **Novo** e adicione o caminho completo para a pasta (ex.: `C:\Terraform`).
   - Clique em **OK** em todas as janelas para confirmar as alterações.

3. **Verificação da instalação:**

   Abra o **Prompt de Comando** ou **PowerShell** e digite:
   ```
   terraform version
   ```
   Se a instalação estiver correta, será exibida a versão instalada do Terraform.

---

## Parte 2 – Instalação e Configuração do AWS CLI

### 2.1 Baixando o AWS CLI

1. **Acesse a página oficial:**  
   Visite o link para a instalação do AWS CLI para Windows:  
   https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

2. **Download do instalador:**  
   Baixe o instalador MSI (o arquivo para Windows) e execute-o.

### 2.2 Instalando o AWS CLI

1. **Instale o AWS CLI:**  
   Siga as instruções do instalador. Ao final, o AWS CLI estará instalado no seu sistema.

2. **Verificação da instalação:**  
   Abra um novo prompt de comando e execute:
   ```
   aws --version
   ```
   O comando deverá retornar a versão do AWS CLI, confirmando que a instalação foi bem-sucedida.

### 2.3 Configurando as Credenciais da AWS

Você tem duas abordagens para configurar as credenciais que serão utilizadas tanto pelo AWS CLI quanto pelo Terraform:

#### Opção A – Usando o Comando `aws configure`

1. **Abra o prompt de comando** e digite:
   ```
   aws configure
   ```
2. **Insira os dados solicitados:**
   - **AWS Access Key ID:** (insira sua chave de acesso)
   - **AWS Secret Access Key:** (insira sua chave secreta)
   - **Default region name:** (exemplo: `us-east-1`, `sa-east-1` ou outra região de sua preferência)
   - **Default output format:** (exemplo: `json`, `text` ou `table`)

   Os dados serão salvos no arquivo de credenciais localizado em `%USERPROFILE%\.aws\credentials`, utilizando o perfil **default**.

#### Opção B – Usando Variáveis de Ambiente

1. **Abra as Configurações de Variáveis de Ambiente:**  
   Acesse Painel de Controle → Sistema → Configurações avançadas do sistema → Variáveis de Ambiente.
2. **Adicione as seguintes variáveis:**
   - `AWS_ACCESS_KEY_ID` – sua chave de acesso.
   - `AWS_SECRET_ACCESS_KEY` – sua chave secreta.
   - *(Opcional)* `AWS_SESSION_TOKEN` – se estiver usando credenciais temporárias.
3. **Confirme e abra um novo prompt de comando** para que as variáveis sejam reconhecidas.

---

## Parte 3 – Integração do Terraform com a AWS e Testes

### 3.1 Configuração do Provider no Terraform

Crie um arquivo de configuração do Terraform, por exemplo, `main.tf`, com o seguinte conteúdo:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"  # Escolha a versão conforme sua necessidade
    }
  }
}

provider "aws" {
  region  = "us-east-1"   # Defina a região desejada
  profile = "default"     # Utilize o perfil configurado (caso tenha usado 'aws configure')
}
```

Este arquivo informa ao Terraform que você usará o provider da AWS e define a região e o perfil a ser utilizado.

### 3.2 Inicializando o Terraform

No diretório onde o `main.tf` está salvo, abra o prompt de comando e execute:
```
terraform init
```
Este comando baixa o provider da AWS e prepara o ambiente para que o Terraform possa operar corretamente.

### 3.3 Testando a Configuração

Para verificar se a configuração está correta e as credenciais estão funcionando, execute:
```
terraform plan
```
O comando `terraform plan` simula a execução e exibe um resumo das operações que serão realizadas (sem realmente aplicar as alterações). Se houver erros de autenticação ou configuração, eles serão apontados nessa etapa.

---

## Considerações Finais e Boas Práticas

- **Segurança:**  
  Mantenha suas credenciais seguras. Evite expô-las em repositórios públicos ou em locais de fácil acesso. Use arquivos protegidos ou variáveis de ambiente para melhor segurança.

- **Múltiplos Perfis:**  
  Se você gerencia mais de uma conta AWS, configure múltiplos perfis no arquivo `%USERPROFILE%\.aws\credentials` e utilize a propriedade `profile` no bloco do provider do Terraform para especificar o perfil desejado.

- **Documentação:**  
  Sempre consulte as documentações oficiais para atualizações e detalhes adicionais:
  - [Documentação do Terraform](https://www.terraform.io/docs)
  - [Documentação do Provider AWS no Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs#authentication)
  - [Documentação do AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
