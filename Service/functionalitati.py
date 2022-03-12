from jsonpickle import json
import json
import Domain
from Domain import tranzactie
from Domain.tranzactie import Tranzactie
from Repository.file_repository import FileRepository
from ViewModels.client_view_models import ClientViewModel
from ViewModels.masina_view_models import MasinaViewModel
from ViewModels.tranzactie_view_models import TranzactieViewModel


class Functionalitati:

    def __init__(self, tranzactii_repository: FileRepository, masini_repository: FileRepository, clienti_repository: FileRepository):
        self.__tranzactii_repository = tranzactii_repository
        self.__masini_repository = masini_repository
        self.__clienti_repository = clienti_repository

    def get_all_tranzactii(self):
        view_models = []
        for tranzactie in self.__tranzactii_repository.get_all():
            masina = self.__masini_repository.get_by_id(tranzactie.id_masina)
            client = self.__clienti_repository.get_by_id(tranzactie.id_card_client)
            view_models.append(TranzactieViewModel(tranzactie.id_entitate, masina, client, tranzactie.suma_piese, tranzactie.suma_manopera, tranzactie.data, tranzactie.ora))

        return view_models

    def get_all_masini(self):
        view_models = []
        for masina in self.__masini_repository.get_all():
            masina = self.__masini_repository.get_by_id(masina.id_entitate)
            view_models.append(MasinaViewModel(masina.id_entitate, masina.model, masina.an_achizitie, masina.nr_km, masina.garantie))
        return view_models

    def get_all_clienti(self):
        view_models = []
        for client in self.__clienti_repository.get_all():
            client = self.__clienti_repository.get_by_id(client.id_entitate)
            view_models.append(ClientViewModel(client.id_entitate, client.nume, client.prenume, client.cnp, client.data_nasterii, client.data_inregistrarii))
        return view_models

    def cautare(self, cuvant_cheie):
        lista = []
        for o_masina in self.get_all_masini():
            if str(o_masina.id_masina) == cuvant_cheie or str(o_masina.model) == cuvant_cheie or str(o_masina.an_achizitie) == cuvant_cheie or str(o_masina.nr_km) == cuvant_cheie or str(o_masina.garantie) == cuvant_cheie:
                lista.append(o_masina)
        for un_client in self.get_all_clienti():
            if str(un_client.id_card_client) == cuvant_cheie or str(un_client.nume) == cuvant_cheie or str(un_client.prenume) == cuvant_cheie or str(un_client.cnp) == cuvant_cheie or str(un_client.data_nasterii) == cuvant_cheie or str(un_client.data_inregistrarii) == cuvant_cheie:
                lista.append(un_client)
        return lista

    def ordonare_suma_manopera(self):
        lista_masini = []
        tranzactii = self.get_all_tranzactii()
        sorted_obj= sorted(tranzactii, key=lambda x: x.suma_manopera, reverse=True)
        for tranzactii_sortate in sorted_obj:
            lista_masini.append(tranzactii_sortate.masina)
        return lista_masini

    #####################################
    def ordonare_suma_manopera_sortare(self):
        tranzactii_lista = self.get_all_tranzactii()
        lista = []
        for x in range (len(tranzactii_lista)-1, 0, -1):
            if tranzactii_lista[x].suma_manopera != None:
                lista.append(tranzactii_lista[x])
        for x in range (len(lista)-1, 0, -1):
            for i in range(x):
                if lista[i].suma_manopera < lista[i+1].suma_manopera:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
        for tranzactie in lista:
            return(tranzactie.masina)

     #########################################
    def ordonare_card_client_sortare(self):
        tranzactii_lista = self.get_all_tranzactii()
        lista = []
        for x in range (len(tranzactii_lista)-1, 0, -1):
            if (tranzactii_lista[x].suma_manopera//10 + tranzactii_lista[x].suma_piese) != None:
                lista.append(tranzactii_lista[x])
        for x in range (len(lista)-1, 0, -1):
            for i in range(x):
                if (lista[i].suma_manopera//10 + lista[i].suma_piese) < (lista[i+1].suma_manopera//10 + lista[i+1].suma_piese):
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
        for tranzactie in lista:
            return(tranzactie.client)


    def ordonare_card_client(self):
        lista_clienti = []
        tranzactii = self.get_all_tranzactii()
        sorted_obj  =sorted(tranzactii, key=lambda x: (x.suma_manopera), reverse=True)
        for tranzactii_sortate in sorted_obj:
            lista_clienti.append(tranzactii_sortate.client)
        return lista_clienti

    def suma_tranzactii_interval(self, st_interval, dr_interval):
        lista = []
        for o_tranzactie in self.get_all_tranzactii():
            suma = o_tranzactie.suma_piese + o_tranzactie.suma_manopera
            if st_interval < suma and dr_interval > suma:
                lista.append(o_tranzactie)
        return lista

#########################
    def suma_tranzactii_interval_map(self, st_interval, dr_interval):
        lista = []
        for o_tranzactie in self.get_all_tranzactii():
            suma = map(lambda suma_piese, suma_manopera: suma_piese + suma_manopera, self.get_all_tranzactii())
            if st_interval < suma and dr_interval > suma:
                lista.append(o_tranzactie)
        return lista


    def stergere_interval_zile(self, st_interval, dr_interval):
        lista = []
        for o_tranzactie in self.get_all_tranzactii():
            data_str = str(o_tranzactie.data)
            zi = int(data_str.split('.')[2])
            if zi < st_interval or zi > dr_interval:
                lista.append(o_tranzactie)
        return lista

    ######################
    def stergere_interval_zile_filter(self, st_interval, dr_interval):
        lista = []
        for o_tranzactie in self.get_all_tranzactii():
            data_str = str(o_tranzactie.data)
            zi = int(data_str.split('.')[2])
            rezultat = filter(lambda zi: zi<st_interval and zi>dr_interval, self.get_all_tranzactii())
            if rezultat is not None:
                lista.append(o_tranzactie)
        return lista


    def actualizare_garantie(self):
        lista = []
        for o_masina in self.get_all_masini():
            if 2020 - int(o_masina.an_achizitie) <= 3 and int(o_masina.nr_km) <= 600000:
                o_masina.garantie = 'da'
            else:
                o_masina.garantie = 'nu'
            lista.append(o_masina)
        return lista


