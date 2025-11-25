from Classes import Lancamento 
class Despesa(Lancamento): # Lancamento tipo despesa
    def __str__(self):
        return f"Despesa({self.valor}, {self.data}, categoria={self.categoria.nome})"
