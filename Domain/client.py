from datetime import datetime

from Domain.entitate import Entitate


class Client(Entitate):
    def __init__(self, id_card_client, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        super().__init__(id_card_client)
        self.__nume = nume
        self.__prenume=prenume
        self.__cnp=cnp
        self.__data_nasterii = data_nasterii
        year, month, day = map(int, data_nasterii.split('.'))
        date = datetime(year, month, day)
        #self.__data_nasterii=datetime.strptime(data_nasterii, '%d.%m.%y')
        #self.__data_inregistrarii=datetime.strptime(data_inregistrarii, '%d.%m.%y')
        self.__data_inregistrarii = data_inregistrarii
        year, month, day = map(int, data_inregistrarii.split('.'))
        date = datetime(year, month, day)

    def __str__(self):
        return f"ID: {self.id_entitate}, nume: {self.nume}, prenume: {self.prenume}, " \
                f"CNP: {self.cnp}, data nasterii: {self.data_nasterii}, data inregistrarii: {self.data_inregistrarii}"


    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, nume_nou):
        self.__nume = nume_nou

    @property
    def prenume(self):
        return self.__prenume

    @prenume.setter
    def prenume(self, prenume_nou):
        self.__prenume = prenume_nou

    @property
    def cnp(self):
        return self.__cnp

    @cnp.setter
    def cnp(self, cnp_nou):
        self.__cnp = cnp_nou

    @property
    def data_nasterii(self):
        return self.__data_nasterii

    @data_nasterii.setter
    def data_nasterii(self, data_nasterii_noua):
        self.__data_nasterii = data_nasterii_noua

    @property
    def data_inregistrarii(self):
        return self.__data_inregistrarii

    @data_inregistrarii.setter
    def data_inregistrarii(self, data_inregistrarii_noua):
        self.__data_inregistrarii = data_inregistrarii_noua