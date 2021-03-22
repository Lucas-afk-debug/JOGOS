from cliente import Cliente
from cliente import c1
from cliente import c2
from imovel import Imovel
from imovel import i1
from imovel import i2
from banco import Banco
from banco import b1
from banco import b2

class Financiamento:
    #CONSTRUTOR
    def __init__(self, cliente, imovel, banco, valor_financiamento, num_aportes):
        self.cliente = cliente
        self.imovel = imovel
        self.banco = banco
        self.valor_financiamento = float(valor_financiamento)
        self.num_aportes = int(num_aportes)
    
    #GETTERS
    def get_cliente(self):
        return self.cliente
    
    def get_imovel(self):
        return self.imovel
    
    def get_banco(self):
        return self.banco
    
    def get_valor_financiamento(self):
        return float(self.valor_financiamento)
    
    def get_num_aportes(self):
        return int(self.num_aportes)
    
    #SETTERS
    def set_cliente(self, novo_cliente):
        self.cliente = novo_cliente

    def set_imovel(self, novo_imovel):
        self.imovel = novo_imovel
    
    def set_banco(self, novo_banco):
        self.banco = novo_banco
    
    def set_valor_financiamento(self, novo_valor_financiamento):
        self.valor_financiamento = float(novo_valor_financiamento)
    
    def set_num_aportes(self, novo_num_aportes):
        self.num_aportes = int(novo_num_aportes)
    
    #MÉTODOS
    def receber_aporte(self, valor):
        if valor >= 0:
            self.num_aportes += 1
            self.valor_financiamento -= valor
            return f'Aqui está o valor atual do financiamento: {self.valor_financiamento}'
    
    #__STR__
    def __str__(self):
        return f'---{self.cliente}---\n{self.banco}\n{self.imovel}\nFinanciamento Total do Imóvel: {self.valor_financiamento}\nNúmero de Aportes: {self.num_aportes}'

f1 = Financiamento(c1, i1, b1, 5000, 0)
f2 = Financiamento(c2, i2, b2, 10000, 0)

