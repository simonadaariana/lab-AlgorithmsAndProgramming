from Domain.tranzactie import Tranzactie
from Repository.file_repository import FileRepository
from ViewModels.tranzactie_view_models import TranzactieViewModel


class TranzactieService:
    def __init__(self, tranzactii_repository: FileRepository, masini_repository: FileRepository, clienti_repository: FileRepository):
        self.__tranzactii_repository = tranzactii_repository
        self.__masini_repository = masini_repository
        self.__clienti_repository = clienti_repository

    def get_all(self):
        view_models = []
        for tranzactie in self.__tranzactii_repository.get_all():
            masina = self.__masini_repository.get_by_id(tranzactie.id_masina)
            client = self.__clienti_repository.get_by_id(tranzactie.id_card_client)
            view_models.append(TranzactieViewModel(tranzactie.id_entitate, masina, client, tranzactie.suma_piese, tranzactie.suma_manopera, tranzactie.data, tranzactie.ora))

        return view_models

    def adaugare(self, id_tranzactie, id_masina, id_card_client, suma_piese, suma_manopera, data, ora):
        tranzactie = Tranzactie(id_tranzactie, id_masina, id_card_client, suma_piese, suma_manopera, data, ora)

        if self.__masini_repository.get_by_id(id_masina) is None:
            raise KeyError('Nu se poate realiza tranzactia pentru ca nu exista o masina cu id-ul ', id_masina)
        if self.__clienti_repository.get_by_id(id_card_client) is None:
            raise KeyError('Nu se poate realiza tranzactia pentru ca nu exista un client cu id-ul ', id_card_client)
        if self.__clienti_repository.get_by_id(id_card_client) is not None:
            tranzactie.suma_manopera_noua = tranzactie.suma_manopera - tranzactie.suma_manopera//10

        self.__tranzactii_repository.adaugare(tranzactie)

    def stergere(self, id_card_client):
        self.__tranzactii_repository.stergere(id_card_client)

    def modificare(self, id_tranzactie, id_masina, id_card_client, suma_piese, suma_manopera, data, ora):
        tranzactie = self.__tranzactii_repository.get_by_id(id_tranzactie)
        if tranzactie is None:
            raise KeyError(f"Nu exista nicio tranzactie cu id-ul {id_tranzactie}")

        if id_masina != '':
            if self.__masini_repository.get_by_id(id_masina) is None:
                raise KeyError('Nu se poate crea comanda, pt. ca nu exista o masina cu id-ul ', id_masina)
            tranzactie.id_masina = id_masina
        if id_card_client != '':
            if self.__clienti_repository.get_by_id(id_card_client) is None:
                raise KeyError('Nu se poate realiza tranzactie pentru ca nu exista un client cu id-ul ', id_card_client)
            tranzactie.id_client = id_card_client
        if suma_piese != '':
            tranzactie.suma_piese = suma_piese
        if suma_manopera != 0:
            tranzactie.suma_manopera = suma_manopera
            if id_card_client != '':
                tranzactie.suma_manopera_noua = tranzactie.suma_manopera - tranzactie.suma_manopera // 10
        if data != 0:
            tranzactie.data = data
        if ora != '':
            tranzactie.ora = ora

        self.__tranzactii_repository.modificare(tranzactie)

    def merge(self, array, left_index, right_index, middle, comparison_function):
        left_copy = array[left_index:middle + 1]
        right_copy = array[middle + 1:right_index + 1]
        left_copy_index = 0
        right_copy_index = 0
        sorted_index = left_index

        while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
            if comparison_function(left_copy[left_copy_index], right_copy[right_copy_index]):
                array[sorted_index] = left_copy[left_copy_index]
                left_copy_index = left_copy_index + 1
            else:
                array[sorted_index] = right_copy[right_copy_index]
                right_copy_index = right_copy_index + 1

            sorted_index = sorted_index + 1

        while left_copy_index < len(left_copy):
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
            sorted_index = sorted_index + 1

        while right_copy_index < len(right_copy):
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
            sorted_index = sorted_index + 1

    def merge_sort(self, array, left_index, right_index, comparison_function):
        if left_index >= right_index:
            return

        middle = (left_index + right_index) // 2
        self.merge_sort(array, left_index, middle, comparison_function)
        self.merge_sort(array, middle + 1, right_index, comparison_function)
        self.merge(array, left_index, right_index, middle, comparison_function)
