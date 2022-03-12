from Domain.client import Client
from Domain.masina import Masina


class TranzactieViewModel:
    def __init__(self, id_tranzactie, masina: Masina, client: Client, suma_piese, suma_manopera, data, ora):
        self.id_tranzactie = id_tranzactie
        self.masina = masina
        self.client = client
        if masina.garantie == 'da':
            self.suma_piese = 0
        else:
            self.suma_piese = suma_piese
        if client.id_entitate is not None:
            self.suma_manopera = suma_manopera - suma_manopera//10
        else:
            self.suma_manopera = suma_manopera
        self.data = data
        self.ora = ora

    def __str__(self):
        return f'ID tranzactie:{self.id_tranzactie} \n-------masina {self.masina} \n-------clientul {self.client} \n ------suma piese: {self.suma_piese}, '\
                f'suma manopera: {self.suma_manopera}, data: {self.data}, ora: {self.ora} '