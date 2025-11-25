class Config: # configuracoes do sistema 
    def __init__(self, valor_minimo_alerta, mes_comparativos, meta_economia):
        self._valor_minimo_alerta = valor_minimo_alerta
        self._mes_comparativos = mes_comparativos
        self._meta_economia = meta_economia

    @property
    def valor_minimo_alerta(self):
        return self._valor_minimo_alerta

    @property
    def mes_comparativos(self):
        return self._mes_comparativos

    @property
    def meta_economia(self):
        return self._meta_economia

    def alterar(self, minimo=None, comparativos=None, economia=None):
        if minimo is not None:
            self._valor_minimo_alerta = minimo
        if comparativos is not None:
            self._mes_comparativos = comparativos
        if economia is not None:
            self._meta_economia = economia

    def __str__(self):
        return "Configurações do Sistema"

    def __eq__(self, other):
        if not isinstance(other, Config):
            return False
        return (
            self.valor_minimo_alerta == other.valor_minimo_alerta and
            self.mes_comparativos == other.mes_comparativos and
            self.meta_economia == other.meta_economia
        )
