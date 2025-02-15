from fastapi import FastAPI, HTTPException
from faker import Faker
from custom_providers import PizzaProvider, BebidaProvider
import random
import uuid
from datetime import datetime, timedelta
from contextlib import asynccontextmanager
from typing import List, Dict

# Instanciação do Faker e adição dos provedores personalizados
faker = Faker(["pt-BR"])
faker.add_provider(PizzaProvider)
faker.add_provider(BebidaProvider)

pedidos: List[Dict] = []  # Lista para armazenar os pedidos gerados

def gerar_data_pedido() -> datetime:
    """
    Gera uma data aleatória para um pedido, dentro de um intervalo de até 60 dias atrás,
    com uma hora, minuto e segundo aleatórios.

    Retorna:
        datetime: A data gerada para o pedido.
    """
    dias = random.randint(0, 60)
    data_aleatorio = datetime.today() - timedelta(days=dias)
    
    hora = random.randint(18, 22)
    minuto = random.randint(0, 59)
    segundo = random.randint(0, 59)
    
    data_pedido = data_aleatorio.replace(hour=hora, minute=minuto, second=segundo, microsecond=0)
    
    return data_pedido


def gerar_pedido() -> Dict:
    """
    Gera um pedido aleatório, com informações como ID do pedido, cliente, data do pedido, forma de pagamento,
    canal de venda e itens do pedido (pizza ou bebida).

    Retorna:
        Dict: Dicionário contendo todas as informações do pedido gerado.
    """
    FORMAS_PAGAMENTO = ['Crédito', 'Débito', 'Dinheiro', 'PIX', 'Voucher']
    CANAIS_VENDA = ['Telefone', 'iFood', 'Caixa']
    
    pedido_id = str(uuid.uuid4())
    cliente = faker.name()
    data_pedido = gerar_data_pedido().strftime('%Y-%m-%d %H:%M:%S')
    forma_pagamento = random.choice(FORMAS_PAGAMENTO)
    canal_venda = random.choice(CANAIS_VENDA)
    
    itens = []
    for _ in range(random.randint(1, 4)):
        if random.random() > 0.5:
            produto = faker.pizza()
        else:
            produto = faker.bebida()
    
        qtd_produto = random.randint(1, 3)
        valor_total = produto['valor_un'] * qtd_produto
        
        itens.append({
            'item_pedido_id': str(uuid.uuid4()),
            'cod_produto': produto['cod'],
            'produto': produto['pizza'] if 'pizza' in produto else produto['bebida'],
            'qtd_produto': qtd_produto,
            'valor_un': produto['valor_un'],
            'valor_total': valor_total,
        })
        
    pedido = {
        'pedido_id': pedido_id,
        'cliente': cliente,
        'data_pedido': data_pedido,
        'forma_pagamento': forma_pagamento,
        'canal_venda': canal_venda,
        'itens': itens
    }
    
    return pedido


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação FastAPI, criando pedidos aleatórios no início
    e finalizando-os quando a API for encerrada.

    Parâmetros:
        app (FastAPI): Instância da aplicação FastAPI.
    """
    global pedidos
    print("Gerando pedidos no startup...")
    num_pedidos = random.randint(4000, 5000)
    pedidos = [gerar_pedido() for _ in range(num_pedidos)]
    print(f'{num_pedidos} pedidos foram gerados!')
    yield
    print('API Finalizando...')

app = FastAPI(lifespan=lifespan)

@app.get('/pedidos')
async def get_pedidos(skip: int = 0, limit: int = 50):
    """
    Endpoint para obter pedidos com paginação.

    Parâmetros:
        skip (int): Número de pedidos a serem pulados (padrão é 0).
        limit (int): Número de pedidos a serem retornados (padrão é 50).

    Retorna:
        Dict[str, any]: Dicionário contendo o total de pedidos e a lista dos pedidos.
    """
    # Aplica a paginação nos pedidos
    pedidos_paginados = pedidos[skip: skip + limit]

    return {'total_pedidos': len(pedidos), 'pedidos': pedidos_paginados}

@app.get('/pedidos/{pedido_id}')
async def get_pedido(pedido_id: str):
    """
    Endpoint para obter um pedido específico através do seu ID.

    Parâmetros:
        pedido_id (str): ID do pedido a ser buscado.

    Retorna:
        Dict[str, any]: Dicionário contendo as informações do pedido, ou um erro 404 caso não encontrado.
    """
    pedido = next((p for p in pedidos if p['pedido_id'] == pedido_id), None)
    if pedido:
        return pedido
    raise HTTPException(status_code=404, detail='Pedido não encontrado')