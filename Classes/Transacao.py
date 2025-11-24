class Lancamento: # Classe base dos Lancamentos
    def __init__(self, valor, categoria, data, descricao, forma_pagamento):
        self.valor = valor
        self.categoria = categoria
        self.data = data
        self.descricao = descricao
        self.forma_pagamento = forma_pagamento

class Receita(Lancamento): # Transacao do tipo receita 
    pass

class Despesa(Lancamento): # Transacao tipo despesa

    pass
