class Depreciacion:
    def __init__(self, valorMaquinaria, valorDesecho, valorVidaUtil):
        self.valorMaquinaria = valorMaquinaria
        self.valorDesecho = valorDesecho
        self.valorVidaUtil = valorVidaUtil

    def calcularDepreciacionAnual(self):
        return (self.valorMaquinaria - self.valorDesecho) / self.valorVidaUtil

