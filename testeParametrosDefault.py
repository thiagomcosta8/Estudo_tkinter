class Teste:
    def __init__(self, nome='default'):
        self.NomeClasse = nome

Povo1 = Teste(nome = 'Thiago')
print(Povo1.NomeClasse)

Povo2 = Teste()
print(Povo2.NomeClasse)