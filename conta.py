from cliente import Cliente
from cliente import c1
from cliente import c2

c1 = Cliente('lucas',71390425436, 1400,[100,200,300,400])
c2 = Cliente('teste', 12345678910, 9999999, [1000,2000,3000,4000])


class Conta:
    #CONSTRUTOR
    def __init__(self, saldo, id, cliente):
        self.saldo = float(saldo)
        self.id = int(id)
        self.cliente = cliente

    #GETTERS
    def get_saldo(self):
        return float(self.saldo)
    
    def get_id(self):
        return int(self.id)
    
    def get_cliente(self):
        return self.cliente
    
    #SETTERS
    def set_saldo(self, novo_saldo):
        self.saldo = float(novo_saldo)

    def set_id(self, novo_id):
        self.id = int(novo_id)
    
    def set_cliente(self, novo_cliente):
        self.cliente = novo_cliente
    
    #MÉTODOS
    def creditar(self, valor):
        if valor > 0:
            self.saldo += valor
        
        return f'Foi creditado {valor} na sua conta\nSaldo atual: {self.saldo}'
    
    def debitar(self, valor):
        if valor > 0:
            self.saldo -= valor
        
        return f'Foi debitado {valor} de sua conta\nSaldo atual: {self.saldo}'

    def transferencia(self, valor, outra_conta):
        if self.saldo >= valor:
            self.saldo -= valor
            outra_conta.creditar(valor)

    #__STR__
    def __str__(self):
        return f'---{self.cliente}---\nSaldo: {self.saldo}\nID: {self.id}\n------------'

ct1 = Conta(500, 1, c1)
ct2 = Conta(1000000, 2, c2)

