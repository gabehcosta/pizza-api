
# API de Simulação de Pedidos de Pizzaria

Este projeto é uma API em FastAPI que simula um sistema de pedidos de pizzaria, com o intuito de gerar dados sintéticos para serem usados em ETLs, análises de dados e na criação de dashboards. A API permite gerar pedidos aleatórios que contêm pizzas e bebidas, utilizando o Faker para gerar dados fictícios. Ela também oferece endpoints para acessar os pedidos gerados e obter informações detalhadas sobre eles.

## Funcionalidades

- **Geração de Pedidos Aleatórios:** A API gera pedidos aleatórios, com informações como ID, cliente, data do pedido, forma de pagamento, canal de venda, e itens (pizza ou bebida).
- **Paginação de Pedidos:** A API implementa paginação para retornar um número limitado de pedidos por vez, facilitando a consulta e análise dos dados.
- **Dados Sintéticos:** A aplicação utiliza o Faker e provedores personalizados para gerar pizzas e bebidas com preços e características aleatórias.

## Endpoints

### `/pedidos`

Este endpoint retorna todos os pedidos gerados, com suporte a paginação.

**Método:** GET

**Parâmetros de consulta:**
- `skip`: Número de pedidos a serem pulados (padrão é 0).
- `limit`: Número de pedidos a serem retornados (padrão é 50).

**Exemplo de uso:**

Para obter os primeiros 50 pedidos:
```
GET /pedidos?skip=0&limit=50
```

Para obter os pedidos 51 a 100:
```
GET /pedidos?skip=50&limit=50
```

### `/pedidos/{pedido_id}`

Este endpoint retorna um pedido específico com base no seu ID.

**Método:** GET

**Parâmetros de URL:**
- `pedido_id`: ID do pedido a ser buscado.

**Exemplo de uso:**
```
GET /pedidos/{pedido_id}
```

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/gabehcosta/pizza-api.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   uvicorn main:app --reload
   ```

A API estará disponível em `http://127.0.0.1:8000`.

Assim como sua documentação interativa, que estará disponível em `http://127.0.0.1:8000/docs`.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
