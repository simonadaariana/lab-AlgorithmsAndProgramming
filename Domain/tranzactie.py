from Domain.entitate import Entitate


class Tranzactie(Entitate):
    def __init__(self, id_tranzactie, id_masina, id_card_client, suma_piese, suma_manopera, data, ora):
        super().__init__(id_tranzactie)
        self.__id_masina = id_masina
        self.__id_card_client = id_card_client
        self.__suma_piese = suma_piese
        self.__suma_manopera = suma_manopera
        self.__data = data
        self.__ora = ora

    @property
    def id_masina(self):
        return self.__id_masina

    @id_masina.setter
    def id_masina(self, id_masina_nou):
        self.__id_masina = id_masina_nou

    @property
    def id_card_client(self):
        return self.__id_card_client

    @id_card_client.setter
    def id_card_client(self, id_card_client_nou):
        self.__id_card_client = id_card_client_nou

    @property
    def suma_piese(self):
        return self.__suma_piese

    @suma_piese.setter
    def suma_piese(self, suma_piese_noua):
        self.__suma_piese = suma_piese_noua

    @property
    def suma_manopera(self):
        return self.__suma_manopera

    @suma_manopera.setter
    def suma_manopera(self, suma_manopera_noua):
        self.__suma_manopera = suma_manopera_noua

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data_noua):
        self.__data = data_noua

    @property
    def ora(self):
        return self.__ora

    @ora.setter
    def ora(self, ora_noua):
        self.__ora = ora_noua

