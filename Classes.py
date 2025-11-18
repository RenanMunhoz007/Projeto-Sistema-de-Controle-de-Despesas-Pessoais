class Categoria: # Representa a categoria da receita ou despesa
    def __init__(self, nome, tipo, limite_mes, descricao): 
        self.nome = nome
        self.tipo = tipo
        self.limite_mes = limite_mes
        self.descricao = descricao

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

class OrcamentoMes: # representa o orcamento do mes

    def __init__(self, ano, mes, definir_orcamento, definit_valor):
        self.ano = ano
        self.mes = mes
        self.definir_orcamento = definir_orcamento
        self.definir_valor = definit_valor

class Alerta: # alerta gerado quando o orcamento passa
    def __init__(self, mensagem, tipo, data):
        self.mensagem = mensagem
        self.tipo = tipo
        self.data = data

class Config: # configuracoes do sistema 
    def __init__(self, valor_minimo_alerta, mes_comparativos, meta_economia):
        self.valor_minimo_alerta = valor_minimo_alerta
        self.mes_comparativos = mes_comparativos
        self.meta_economia = meta_economia 
