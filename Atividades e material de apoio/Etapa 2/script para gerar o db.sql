DROP TABLE IF EXISTS Clientes;
CREATE TABLE Clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cidade TEXT NOT NULL
);

DROP TABLE IF EXISTS Pedidos;
CREATE TABLE Pedidos (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    valor REAL NOT NULL,
    data_pedido DATE NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

DROP TABLE IF EXISTS Produtos;
CREATE TABLE Produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT NOT NULL,
    preco REAL NOT NULL
);

DROP TABLE IF EXISTS ItensPedido;
CREATE TABLE ItensPedido (
    id_item INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pedido INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES Produtos(id_produto)
);

INSERT INTO Clientes (nome, cidade) VALUES
  ('Ana', 'São Paulo'),
  ('João', 'Rio de Janeiro'),
  ('Maria', 'Belo Horizonte'),
  ('Pedro', 'Curitiba'),
  ('Carla', 'Porto Alegre');

INSERT INTO Pedidos (id_cliente, valor, data_pedido) VALUES
  (1, 150.00, '2024-11-01'),
  (1, 50.00, '2024-11-04'),
  (1, 120.00, '2024-11-06'),
  (2, 200.00, '2024-11-02'),
  (2, 180.00, '2024-11-07'),
  (3, 75.00, '2024-11-03'),
  (4, 300.00, '2024-11-05'),
  (4, 250.00, '2024-11-08'),
  (5, 220.00, '2024-11-09'),
  (5, 190.00, '2024-11-10'),
  (5, 210.00, '2024-11-11');

INSERT INTO Produtos (nome_produto, preco) VALUES
  ('Notebook', 3000.00),
  ('Mouse', 50.00),
  ('Teclado', 100.00),
  ('Monitor', 800.00),
  ('Impressora', 1200.00);

INSERT INTO ItensPedido (id_pedido, id_produto, quantidade) VALUES
  (1, 1, 1),
  (1, 2, 2),
  (2, 3, 1),
  (3, 4, 1),
  (4, 5, 1),
  (5, 1, 1),
  (6, 2, 3),
  (7, 3, 1),
  (8, 4, 2),
  (9, 5, 1),
  (10, 1, 2),
  (11, 2, 1);
