class Categoria: # Representa a categoria da receita ou despesa
    def __init__(self, nome, tipo, limite_mes=0, descricao=""):
        self._nome = nome
        self._tipo = tipo  
        self._limite_mes = limite_mes
        self._descricao = descricao

    @property
    def nome(self):
        return self._nome

    @property
    def tipo(self):
        return self._tipo

    @property
    def limite_mes(self):
        return self._limite_mes

    @property
    def descricao(self):
        return self._descricao

    def __str__(self):
        return f"Categoria({self.nome}, tipo={self.tipo})"

    def __eq__(self, other):
        if not isinstance(other, Categoria):
            return False
        return self.nome == other.nome and self.tipo == other.tipo
