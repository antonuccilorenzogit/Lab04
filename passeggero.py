class Passeggero:
    def __init__(self, codPasseggero, nomePasseggero, cognomePasseggero):
        self.codPasseggero = codPasseggero
        self.nomePasseggero = nomePasseggero
        self.cognomePasseggero = cognomePasseggero
        self.ha_cabina= False
        self.cabina = None

    def assegna_cabina(self,codCabina):
        self.ha_cabina = True
        self.cabina = codCabina

    def __str__(self):
        return f'Passeggero = {self.codPasseggero} | {self.nomePasseggero} {self.cognomePasseggero}'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.codPasseggero == other
