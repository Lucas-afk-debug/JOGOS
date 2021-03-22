class Cliente:
    #CONSTRUTOR
    def __init__(self, nome, cpf, salario, financiamento):
        self.nome = str(nome)
        self.cpf = str(cpf)
        self.salario = float(salario)
        self.financiamento = financiamento
    
    #GETTERS
    def get_nome(self):
        return str(self.nome).upper()
    
    def get_cpf(self):
        return str(self.cpf)
    
    def get_salario(self):
        return float(self.salario)

    def get_financiamento(self):
        return (self.financiamento)
    
    #SETTERS
    def set_nome(self, novo_nome):
        self.nome = str(novo_nome).upper()

    def set_cpf(self, novo_cpf):
        self.cpf = str(novo_cpf)
    
    def set_salario(self, novo_salario):
        if self.salario >= 0:
            self.salario = float(novo_salario)

    def set_financiamento(self, novo_financiamento):
        self.financiamento = novo_financiamento

    #MÉTODOS
    def total_financiado(self):
        tot= sum(self.financiamento)
        return f'Aqui está o total dos financiamentos: {tot}'
    
    def add_financiamento(self, novo_financiamento):
        self.financiamento.append(novo_financiamento)
        return f'Lista de financiamentos atualizada: \n{self.financiamento}'
    
    #__STR__
    def __str__(self):
        return f'---{self.nome}---\nCPF: {self.cpf}\nSalário: {self.salario}\nFinanciamentos: {self.financiamento}\n---------------'

c1 = Cliente('lucas',71390425436, 1400,[100,200,300,400])
c2 = Cliente('teste', 12345678910, 9999999, [1000,2000,3000,4000])


