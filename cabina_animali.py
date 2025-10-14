from cabina import Cabina

class CabinaAnimali(Cabina):
    def __init__(self,codCabina, numLetti, ponte, prezzo, max_animali,):
        super().__init__(codCabina, numLetti, ponte, prezzo)
        self.max_animali= max_animali

    def nuovo_prezzo(self):
        self.prezzo = int(self.prezzo) * (1 + 0.10* int(self.max_animali))


    def __str__(self):
        return f'{self.codCabina} | {self.numLetti} letti - ponte {self.ponte} - prezzo {self.prezzo} euro - max_animali {self.max_animali}|'

