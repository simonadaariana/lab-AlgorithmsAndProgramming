class ClientViewModel:
    def __init__(self, id_card_client, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        self.id_card_client = id_card_client
        self.nume = nume
        self.prenume = prenume
        self.cnp = cnp
        self.data_nasterii = data_nasterii
        self.data_inregistrarii = data_inregistrarii

    def __str__(self):
        return f'ID card client:{self.id_card_client}, nume: {self.nume}, prenume: {self.prenume}, CNP: {self.cnp}, data nasterii: {self.data_nasterii}, data inregistrarii: {self.data_inregistrarii} '