import numpy as np

class Coordenadas:
    def __init__(self):
        # Criar o array 3 x 3 com números aleatórios entre 1 e 52
        np.random.seed(1)
        self.inicio = np.random.randint(0,10000, (10000,2))
        self.fim = np.random.randint(0,10000, (10000,2))
