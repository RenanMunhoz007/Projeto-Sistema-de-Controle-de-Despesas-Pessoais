class Alerta: # alerta gerado quando o orcamento passa
    def __init__(self, mensagem, tipo, data):
        self._mensagem = mensagem
        self._tipo = tipo
        self._data = data

    @property
    def mensagem(self):
        return self._mensagem

    @property
    def tipo(self):
        return self._tipo

    @property
    def data(self):
        return self._data

    def mostrar(self):
        return f"[{self.tipo}] {self.mensagem} - {self.data}"

    def __str__(self):
        return f"Alerta({self.tipo}, '{self.mensagem}')"

    def __eq__(self, other):
        if not isinstance(other, Alerta):
            return False
        return (
            self.mensagem == other.mensagem and
            self.tipo == other.tipo and
            self.data == other.data
        )
