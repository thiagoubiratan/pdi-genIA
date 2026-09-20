import asyncio
import time

from pydantic import BaseModel


# ETAPA 1 — Definir o que é um Produto
class Produto(BaseModel):
    nome: str
    preco: float


# ETAPA 2 — Criar a lista de produtos disponíveis (usa a Etapa 1)
produto = [
    Produto(nome="Coca cola", preco=3.50),
    Produto(nome="Pizza de filezinho", preco=23.99),
]


# ETAPA 3 — Definir o que é um Pedido (usa produtos da Etapa 1)
class Pedido:
    def __init__(self, produtos):
        self.produtos = produtos

    def calcular_total(self):
        total = 0
        for i in self.produtos:
            total += i.preco
        return total


# ETAPA 4 — Definir um Pedido com entrega (herda da Etapa 3)
class PedidoDelivery(Pedido):
    def __init__(self, produtos, taxa_entrega):
        super().__init__(produtos)  # reaproveita o __init__ da classe pai (Pedido)
        self.taxa_entrega = taxa_entrega

    def calcular_total(self):
        total_produtos = super().calcular_total()  # reaproveita o cálculo da classe pai
        return total_produtos + self.taxa_entrega


# ETAPA 5 — Criar os pedidos de fato (usa Etapas 3 e 4)
pedido1 = Pedido(produto)
pedido2 = PedidoDelivery(produto, taxa_entrega=5.0)

print(f"Total pedido normal: R$ {pedido1.calcular_total():.2f}")
print(f"Total pedido delivery (com taxa): R$ {pedido2.calcular_total():.2f}")


# ETAPA 6 — Decorator para medir tempo (independente, usado na Etapa 7)
def medir_tempo(func):
    def wrapper(*arg, **kwargs):
        inicio = time.time()
        resultado = func(*arg, **kwargs)
        fim = time.time()
        print(f"{func.__name__} executou em {fim - inicio:.4f} segundos")
        return resultado

    return wrapper


# ETAPA 7 — Função que usa o decorator da Etapa 6
@medir_tempo
def processar():
    time.sleep(2)
    print("Processamento concluído")


processar()


# ETAPA 8 — Função assíncrona que processa um pedido (usa Etapa 4/5)
async def processar_pedido(pedido):
    print("Preparando pedido...")
    await asyncio.sleep(2)
    total = pedido.calcular_total()
    print(f"Pedido pronto! Total: R$ {total:.2f}")


asyncio.run(processar_pedido(pedido2))
