from faker.providers import BaseProvider
import random
from typing import Dict

class PizzaProvider(BaseProvider):
    def pizza(self) -> Dict[str, any]:
        """
        Gera uma pizza aleatória com código, nome e valor unitário.

        Retorna:
            Dict[str, any]: Dicionário com os dados da pizza (código, nome e valor unitário).
        """
        pizzas = [
            {'cod': 'P001', 'pizza': 'Pizza de Calabresa', 'valor_un': 55.00},
            {'cod': 'P002', 'pizza': 'Pizza de 4 Queijos', 'valor_un': 70.00},
            {'cod': 'P003', 'pizza': 'Pizza Portuguesa', 'valor_un': 55.00},
            {'cod': 'P004', 'pizza': 'Pizza de Mussarela', 'valor_un': 50.00},
            {'cod': 'P005', 'pizza': 'Pizza Marguerita', 'valor_un': 65.00},
            {'cod': 'P006', 'pizza': 'Pizza de Estrogonofe', 'valor_un': 70.00},
            {'cod': 'P006', 'pizza': 'Pizza de Frango Catupiry', 'valor_un': 60.00},
            {'cod': 'P007', 'pizza': 'Pizza de Filé Mignon', 'valor_un': 135.00}
        ]
        return random.choice(pizzas)
    
class BebidaProvider(BaseProvider):
    def bebida(self) -> Dict[str, any]:
        """
        Gera uma bebida aleatória com código, nome e valor unitário.

        Retorna:
            Dict[str, any]: Dicionário com os dados da bebida (código, nome e valor unitário).
        """
        bebidas = [
            {'cod': 'B001', 'bebida': 'Água Mineral 600ml', 'valor_un': 5.00},
            {'cod': 'B002', 'bebida': 'Água Mineral 1L', 'valor_un': 10.00},
            {'cod': 'B003', 'bebida': 'Coca-Cola 600ml', 'valor_un': 7.00},
            {'cod': 'B004', 'bebida': 'Coca-Cola 1L', 'valor_un': 10.00},
            {'cod': 'B005', 'bebida': 'Coca-Cola 2L', 'valor_un': 12.00},
            {'cod': 'B006', 'bebida': 'Pepsi 600ml', 'valor_un': 8.00},
            {'cod': 'B007', 'bebida': 'Pepsi 1L', 'valor_un': 9.00},
            {'cod': 'B008', 'bebida': 'Pepsi 2L', 'valor_un': 11.00},
            {'cod': 'B009', 'bebida': 'Guaraná Antártica 600ml', 'valor_un': 7.50},
            {'cod': 'B010', 'bebida': 'Guaraná Antártica 1L', 'valor_un': 10.50},
            {'cod': 'B011', 'bebida': 'Guaraná Antártica 2L', 'valor_un': 11.50},
            {'cod': 'B012', 'bebida': 'Suco Del Valle - Uva 1L', 'valor_un': 15.00},
            {'cod': 'B013', 'bebida': 'Suco Del Valle - Pêssego 1L', 'valor_un': 15.00},
            {'cod': 'B014', 'bebida': 'Suco Life - Laranja 1L', 'valor_un': 13.00},
        ]
        return random.choice(bebidas)