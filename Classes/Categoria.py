class Categoria: # Representa a categoria da receita ou despesa
    def __init__(self, nome, tipo, limite_mes, descricao): 
        self.nome = nome
        self.tipo = tipo
        self.limite_mes = limite_mes
        self.descricao = descricao