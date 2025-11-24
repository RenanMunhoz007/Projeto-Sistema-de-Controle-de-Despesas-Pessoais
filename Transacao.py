class Transacao: # Classe base das transacoes
    def __init__(self, valor, categoria, data, descricao, forma_pagamento):
        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.descricao = descricao
        self.forma_pagamento = forma_pagamento

class Receita(Transacao): # Transacao do tipo receita 
    pass

class Despesa(Transacao): # Transacao tipo despesa
    pass