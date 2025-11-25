from Classes import Lancamento
class Receita(Lancamento): # Lancamento do tipo receita 
    def __str__(self):
        return f"Receita({self.valor}, {self.data}, categoria={self.categoria.nome})"
