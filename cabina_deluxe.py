from cabina import Cabina

class Cabina_Deluxe(Cabina):
    def __init__(self, codCabina, numLetti, ponte, prezzo, stile):
        super().__init__(codCabina, numLetti, ponte, prezzo)
        self.stile= stile

    def nuovo_prezzo(self):
        self.prezzo = int(self.prezzo) * 1.20

    def __str__(self):
        return f'{self.codCabina} | {self.numLetti} letti - ponte {self.ponte} - prezzo {self.prezzo} euro - stile {self.stile}|'