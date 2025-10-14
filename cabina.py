class Cabina:
    def __init__(self, codCabina, numLetti, ponte, prezzo):
        self.codCabina = codCabina
        self.numLetti = numLetti
        self.ponte = ponte
        self.prezzo = int(prezzo)
        self.codPasseggero= None
        self.occupata= False

    def associa_passeggero_a_cabina(self, codPasseggero):
        self.codPasseggero = codPasseggero
        self.occupata = True

    def __str__(self):
        return f'{self.codCabina} | {self.numLetti} letti - ponte {self.ponte} - prezzo {self.prezzo} euro|'
    def __eq__(self, other):
        if isinstance(other, str):
            return self.codCabina == other