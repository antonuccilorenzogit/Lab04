from cabina import Cabina
from passeggero import Passeggero
from cabina_animali import CabinaAnimali
from cabina_deluxe import Cabina_Deluxe

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.lista_passeggeri= []
        self.lista_cabine= []

    def __str__(self):
        return f'Crociera rinominata :{self.nome}'

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        infile= open(file_path,'r', encoding='utf-8')
        for riga in infile:
            riga = riga.strip('\n').split(',')

            #Verifico se si tratta di Cabine (semplici, Animali, Deluxe) o Passeggeri e inizializzo gli oggetti
            if len(riga) == 3:
                codPasseggero, nomePasseggero, cognomePasseggero = riga
                passeggero= Passeggero(codPasseggero ,nomePasseggero, cognomePasseggero)
                self.lista_passeggeri.append(passeggero)
            elif len(riga)== 4:
                codCabina, numLetti, ponte, prezzo = riga
                cabina= Cabina(codCabina, numLetti, ponte, prezzo)
                self.lista_cabine.append(cabina)
            elif riga[4].isnumeric():
                codCabina, numLetti, ponte, prezzo, max_animali= riga
                cabina_animali= CabinaAnimali(codCabina, numLetti, ponte, prezzo, max_animali)
                cabina_animali.nuovo_prezzo()
                self.lista_cabine.append(cabina_animali)

            elif riga[4].isalpha():
                codCabina, numLetti, ponte, prezzo, stile = riga
                cabina_deluxe = Cabina_Deluxe(codCabina, numLetti, ponte, prezzo, stile)
                cabina_deluxe.nuovo_prezzo()
                self.lista_cabine.append(cabina_deluxe)

    def trova_passeggero(self, codp):
        for passeggero in self.lista_passeggeri:
            if passeggero.codPasseggero == codp:
                return passeggero
        return None

    def trova_cabina(self, codc):
        for cabina in self.lista_cabine:
            if cabina.codCabina == codc:
                return cabina
        else:
            return None

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""

        if (self.trova_passeggero(codice_passeggero) is not None ) and self.trova_cabina(codice_cabina) is not None:
            cabina= self.trova_cabina(codice_cabina)
            passeggero = self.trova_passeggero(codice_passeggero)
            if (not cabina.occupata) and (not passeggero.ha_cabina):
                passeggero.assegna_cabina(codice_cabina)
                cabina.associa_passeggero_a_cabina(codice_passeggero)
            else:
                raise Exception(f'Passeggero occupato o Cabina occupata')
        else:
            raise Exception('Passeggerio non trovato o/e Cabina non trovata')

        print(f'il passeggero {passeggero.codPasseggero} ha prenotato la cabina {cabina.codCabina}')


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        lista_ordinata = sorted(self.lista_cabine, key=lambda x: x.prezzo)
        return lista_ordinata

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self.lista_passeggeri:
            print(f'{passeggero.nomePasseggero} {passeggero.cognomePasseggero} - {passeggero.cabina}')


