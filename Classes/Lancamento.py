from Classes import Categoria 
class Lancamento: # Classe base dos Lancamentos
    def __init__(self, valor, data, descricao, categoria: Categoria):
        self._valor = valor
        self._data = data
        self._descricao = descricao
        self._categoria = categoria

    @property
    def valor(self):
        return self._valor

    @property
    def data(self):
        return self._data

    @property
    def descricao(self):
        return self._descricao

    @property
    def categoria(self):
        return self._categoria

    def __str__(self):
        return f"Lançamento({self.valor}, {self.data}, '{self.descricao}')"

    def __eq__(self, other):
        if not isinstance(other, Lancamento):
            return False
        return (
            self.valor == other.valor and
            self.data == other.data and
            self.descricao == other.descricao
        )
