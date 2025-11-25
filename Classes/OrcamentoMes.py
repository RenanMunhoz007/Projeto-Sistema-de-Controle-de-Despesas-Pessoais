class OrcamentoMes: # representa o orcamento do mes
    def __init__(self, ano, mes, definir_orcamento=0, definir_valor=0):
        self._ano = ano
        self._mes = mes
        self._definir_orcamento = definir_orcamento
        self._definir_valor = definir_valor
        self._lancamentos = []
        self._alertas = []

    @property
    def ano(self):
        return self._ano

    @property
    def mes(self):
        return self._mes

    @property
    def definir_orcamento(self):
        return self._definir_orcamento

    @property
    def definir_valor(self):
        return self._definir_valor

    @property
    def lancamentos(self):
        return self._lancamentos

    @property
    def alertas(self):
        return self._alertas

    def adicionar_lancamento(self, lanc):
        self._lancamentos.append(lanc)

    def calcular_total(self):
        return sum(l.valor for l in self._lancamentos)

    def __str__(self):
        return f"OrcamentoMes({self.ano}-{self.mes})"

    def __eq__(self, other):
        if not isinstance(other, OrcamentoMes):
            return False
        return self.ano == other.ano and self.mes == other.mes


