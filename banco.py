from conta import Conta
from conta import ct1
from conta import ct2
from conta import c1
from conta import c2

contas = []
contas.append(ct1)
contas.append(ct2)

financiamentos = []
financiamentos.append(c1.financiamento)
financiamentos.append(c2.financiamento)

class Banco:
    #CONSTRUTOR
    def __init__(self, nome_do_banco, contas, financiamentos):
        self.nome_do_banco = str(nome_do_banco)
        self.contas = contas
        self.financiamentos = financiamentos
    
    #GETTERS
    def get_nome_do_banco(self):
        return str(self.nome_do_banco)
    
    def get_contas(self):
        return self.contas
    
    def get_financiamentos(self):
        return self.financiamentos
    
    #SETTERS
    def set_nome_do_banco(self, novo_nome_do_banco):
        self.nome_do_banco = str(novo_nome_do_banco)

    def set_contas(self, novo_contas):
        self.contas = novo_contas
    
    def set_financiamentos(self, novo_financiamentos):
        self.financiamentos = novo_financiamentos

    #MÉTODOS
    def total_valor_contas(self):
        saldo_total = 0
        saldo_total = self.contas[0].saldo + self.contas[1].saldo
        return f'Aqui está o saldo total de todas as contas: {saldo_total}'
    
    def financiamentos_cliente(self, cpf):
        if cpf == self.contas[0].cliente.cpf:
            return f'Aqui está a sua lista de financiamentos:\n{self.contas[0].cliente.financiamento}'
        
        elif cpf == self.contas[1].cliente.cpf:
            return f'Aqui está a sua lista de financiamentos:\n{self.contas[1].cliente.financiamento}'

    #__STR__
    def __str__(self):
        return f'---{self.nome_do_banco}---\nLista de Contas: {self.contas}\nLista de Financiamentos: {self.financiamentos}\n-----------'

b1 = Banco('Nubank', contas, financiamentos)
b2 = Banco('Banco do Brasil', contas, financiamentos)
