# Modelo de Dados - Sistema E-commerce

## Entidades e Atributos

### Usuário (user)
- **id** (INTEGER): Identificador único do usuário (chave primária)
- **name** (TEXT): Nome completo do usuário
- **email** (TEXT): Email do usuário (único)
- **phone** (TEXT): Número de telefone do usuário
- **birth_date** (TEXT): Data de nascimento do usuário
- **creation_date** (TEXT): Data de criação do registro

### Produto (product)
- **id** (INTEGER): Identificador único do produto (chave primária)
- **name** (TEXT): Nome do produto
- **description** (TEXT): Descrição detalhada do produto
- **price** (REAL): Preço do produto
- **category** (TEXT): Categoria do produto
- **stock** (INTEGER): Quantidade disponível em estoque
- **creation_date** (TEXT): Data de criação do registro

### Pedido (order)
- **id** (INTEGER): Identificador único do pedido (chave primária)
- **user_id** (INTEGER): Identificador do usuário que fez o pedido (chave estrangeira)
- **order_date** (TEXT): Data em que o pedido foi realizado
- **status** (TEXT): Status atual do pedido ('pending', 'approved', 'shipped', 'delivered', 'canceled')
- **total_value** (REAL): Valor total do pedido
- **creation_date** (TEXT): Data de criação do registro

### Item de Pedido (order_item)
- **id** (INTEGER): Identificador único do item de pedido (chave primária)
- **order_id** (INTEGER): Identificador do pedido associado (chave estrangeira)
- **product_id** (INTEGER): Identificador do produto associado (chave estrangeira)
- **quantity** (INTEGER): Quantidade do produto no pedido
- **unit_price** (REAL): Preço unitário do produto no momento da compra
- **creation_date** (TEXT): Data de criação do registro

## Relacionamentos

1. **Usuário → Pedido**: Um usuário pode fazer múltiplos pedidos (relacionamento 1:N)
   - Chave estrangeira: `user_id` em `order` referencia `id` em `user`

2. **Pedido → Item de Pedido**: Um pedido pode conter múltiplos itens (relacionamento 1:N)
   - Chave estrangeira: `order_id` em `order_item` referencia `id` em `order`

3. **Produto → Item de Pedido**: Um produto pode estar em múltiplos itens de pedido (relacionamento 1:N)
   - Chave estrangeira: `product_id` em `order_item` referencia `id` em `product`

## Observações

- Todas as tabelas possuem um campo `creation_date` para controle de auditoria
- Pedidos têm um status padrão definido como 'pending'
- Emails de usuários são únicos no sistema
- Produtos têm um estoque padrão de 0 unidades