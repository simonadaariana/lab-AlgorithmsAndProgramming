from Domain.client import Client
from Repository.file_repository import FileRepository


class ClientService:
    def __init__(self, clienti_repository: FileRepository):
        self.__clienti_repository = clienti_repository

    def get_all(self):
        return self.__clienti_repository.get_all()

    def adaugare(self, id_card_client, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        client = Client(id_card_client, nume, prenume, cnp, data_nasterii, data_inregistrarii)
        self.__clienti_repository.adaugare(client)

    def stergere(self, id_card_client):
        self.__clienti_repository.stergere(id_card_client)

    def modificare(self, id_card_client, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        client = self.__clienti_repository.get_by_id(id_card_client)
        if client is None:
            raise KeyError(f"Nu exista niciun client cu id-ul {id_card_client}")

        if nume != "":
            client.nume = nume
        if prenume != "":
            client.prenume = prenume
        if cnp != 0:
            client.cnp = cnp
        if data_nasterii != "":
            client.data_nasterii = data_nasterii
        if data_inregistrarii != "":
            client.data_inregistrarii = data_inregistrarii

        self.__clienti_repository.modificare(client)

