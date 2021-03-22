class Imovel:
    #CONSTRUTOR
    def __init__(self, tipo, valor, codigo):
        self.tipo = str(tipo)
        self.valor = float(valor)
        self.codigo = int(codigo)
    
    #GETTERS
    def get_tipo(self):
        return str(self.tipo)
    
    def get_valor(self):
        return float(self.valor)
    
    def get_codigo(self):
        return int(self.codigo)
    
    #SETTERS
    def set_tipo(self, novo_tipo):
        self.tipo = str(novo_tipo)

    def set_valor(self, novo_valor):
        self.valor = float(novo_valor)
    
    def set_codigo(self, novo_codigo):
        self.codigo = novo_codigo
    
    #__STR__
    def __str__(self):
        return f'---{self.tipo}/{self.codigo}---\nValor: {self.valor}'

i1 = Imovel('Apartamento',40000,1234)
i2 = Imovel('Casa', 200000, 4321)
