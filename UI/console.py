from datetime import datetime
import random
import pandas as pd

from Domain import masina, tranzactie

from Repository.file_repository import FileRepository
from Service.functionalitati import Functionalitati
from Service.tranzactie_service import TranzactieService
from Service.client_service import ClientService
from Service.masina_service import MasinaService
from Service.undo_redo_service import UndoRedoService



class Consola:
    def __init__(self, masina_service: MasinaService, client_service: ClientService,
                 tranzactie_service: TranzactieService, functionalitati: Functionalitati,
                 undo_redo_service: UndoRedoService):
        self.__masina_service = masina_service
        self.__client_service = client_service
        self.__tranzactie_service = tranzactie_service
        self.__functionalitati = functionalitati
        self.__undo_redo_service = undo_redo_service


    def run_menu(self):
        while True:
            print("1. CRUD masini")
            print("2. CRUD clienti")
            print("3. CRUD tranzactii")
            print("4. Functionalitati")
            print('------------------')
            print("x. Iesire")
            optiune = input("Alegeti o optiune: ")
            if optiune == "1":
                self.run_crud_masini()
            elif optiune == "2":
                self.run_crud_clienti()
            elif optiune == "3":
                self.run_crud_tranzactii()
            elif optiune == "4":
                self.run_functionalitati()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def run_functionalitati(self):
        while True:
            print("1. Cautare masini si clienti dupa model, an fabricatie, prenume, CNP etc.")
            print("2. Afisarea tuturor tranzactiilor cu suma cuprinsa intr-un interval dat")
            print("3. Afisarea masinilor ordonate descrescator dupa suma obtinuta pe manopera")
            print("4. Afisarea cardurilor client ordonate descrescator dupa valoarea reducerilor obtinute")
            print("5. Stergerea tuturor tranzactiilor dintr-un anumit interval de zile")
            print("6. Actualizare garantie")
            print("7. Masini in Excel")
            print("-----------------------")
            print("x. Inapoi")
            optiune = input("Alegeti o optiune: ")
            if optiune == "1":
                self.ui_cautare()
            elif optiune == "2":
                self.ui_suma_tranzactii_interval_map()
            elif optiune == "3":
                self.ui_merge_sort()
            elif optiune == "4":
                self.ui_ordonare_card_client()
            elif optiune == "5":
                self.ui_stergere_interval_zile()
            elif optiune == "6":
                self.ui_actualizare_garantie()
            elif optiune == "7":
                self.ui_masini_in_excel()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def run_crud_masini(self):
        while True:
            print("1. Adaugare masina")
            print("2. Stergere masina")
            print("3. Modificare masina")
            print("4. Generare random")
            print("------------------------")
            print("a. Afiseaza toate masinile")
            print("u. Undo")
            print("r. Redo")
            print("x. Inapoi")
            optiune = input("Alegeti o optiune: ")
            if optiune == "1":
                self.ui_adaugare_masina()
            elif optiune == "2":
                self.ui_stergere_masina()
            elif optiune == "3":
                self.ui_modificare_masina()
            elif optiune == "4":
                self.generare_random()
            elif optiune == "a":
                self.ui_afisare_masini()
            elif optiune == "u":
                self.__undo_redo_service.do_undo()
            elif optiune == "r":
                self.__undo_redo_service.do_redo()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def ui_cautare(self):
        cuvant_cheie = input("Introduceti cuvantul cheie: ")
        rezultat = self.__functionalitati.cautare(cuvant_cheie)
        for i in rezultat:
            if i is not None:
                print(i)
            else:
                print("Nu exista client sau masina care sa contina cuvantul cheie dat.")

    def ui_masini_in_excel(self):
        masini = self.__masina_service.get_all()
        dataList = []
        for masina in masini:
            data = {'id masina': masina.id_entitate,
                    'model': masina.model,
                    'an achizitie': masina.an_achizitie,
                    'nr km': masina.nr_km,
                    'garantie': masina.garantie
                    }
            dataList.append(data)
        df = pd.DataFrame(dataList)
        df.to_excel(r'C:\Users\simon\PycharmProjects\lab11\masini.xls', index=False)

    def ui_ordonare_suma_manopera(self):
        rezultat = self.__functionalitati.ordonare_suma_manopera()
        for i in rezultat:
            print(i)

    def ui_ordonare_suma_manopera_sortare(self):
        rezultat = self.__functionalitati.ordonare_suma_manopera()
        for i in rezultat:
            print(i)

    def ui_ordonare_card_client_sortare(self):
        rezultat = self.__functionalitati.ordonare_card_client_sortare()
        for i in rezultat:
            print(i)

    def ui_ordonare_card_client(self):
        rezultat = self.__functionalitati.ordonare_card_client()
        for i in rezultat:
            print(i)

    def ui_suma_tranzactii_interval(self):
        st_interval = float(input("Introduceti capatul din stanga al intervalului: "))
        dr_interval = float(input("Introduceti capatul din dreapta al intervalului: "))
        rezultat = self.__functionalitati.suma_tranzactii_interval(st_interval, dr_interval)
        for i in rezultat:
            if i is not None:
                print(i)
            else:
                print("Nu exista tranzactii a caror suma sa se afle in intervalul dat.")

    def ui_suma_tranzactii_interval_map(self):
        st_interval = float(input("Introduceti capatul din stanga al intervalului: "))
        dr_interval = float(input("Introduceti capatul din dreapta al intervalului: "))
        rezultat = self.__functionalitati.suma_tranzactii_interval(st_interval, dr_interval)
        for i in rezultat:
            if i is not None:
                print(i)
            else:
                print("Nu exista tranzactii a caror suma sa se afle in intervalul dat.")

    def ui_actualizare_garantie(self):
        rezultat = self.__functionalitati.actualizare_garantie()
        for i in rezultat:
            if i is not None:
                print(i)

    def ui_stergere_interval_zile(self):
        st_interval = int(input("Introduceti capatul din stanga al intervalului: "))
        dr_interval = int(input("Introduceti capatul din dreapta al intervalului: "))
        rezultat = self.__functionalitati.stergere_interval_zile(st_interval, dr_interval)
        for i in rezultat:
            if i is not None:
                print(i)

    def ui_stergere_interval_zile_filter(self):
        st_interval = int(input("Introduceti capatul din stanga al intervalului: "))
        dr_interval = int(input("Introduceti capatul din dreapta al intervalului: "))
        rezultat = self.__functionalitati.stergere_interval_zile(st_interval, dr_interval)
        for i in rezultat:
            if i is not None:
                print(i)

    def ui_adaugare_masina(self):
        try:
            id_masina = input("Introduceti ID-ul masinii: ")
            model = input("Introduceti modelul masinii: ")
            an_achizitie = int(input("Introduceti anul achizitiei masinii: "))
            nr_km = int(input("Introduceti numarul de kilometri al masinii: "))
            garantie = input("Mentionati daca masina este in garantie (da, nu): ")

            self.__masina_service.adaugare(id_masina, model, an_achizitie, nr_km, garantie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_stergere_masina(self):
        try:
            id_masina = input("Introduceti ID-ul masinii care se strege: ")

            self.__masina_service.stergere(id_masina)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modificare_masina(self):
        try:
            id_masina = input("Introduceti ID-ul masinii care se modifica: ")
            model = input("Introduceti modelul masinii: ")
            an_achizitie = int(input("Introduceti anul achizitiei masinii: "))
            nr_km = int(input("Introduceti numarul de kilometri al masinii: "))
            garantie = input("Mentionati daca masina este in garantie (da, nu): ")

            self.__masina_service.modificare(id_masina, model, an_achizitie, nr_km, garantie)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare_masini(self):
        masini = self.__masina_service.get_all()
        for masina in masini:
            print(masina)

    def run_crud_clienti(self):
        while True:
            print("1. Adaugare client")
            print("2. Stergere client")
            print("3. Modificare client")
            print("a. Afiseaza toti clientii")
            print("x. Inapoi")
            optiune = input("Alegeti o optiune: ")
            if optiune == "1":
                self.ui_adaugare_client()
            elif optiune == "2":
                self.ui_stergere_client()
            elif optiune == "3":
                self.ui_modificare_client()
            elif optiune == "a":
                self.ui_afisare_clienti()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def ui_adaugare_client(self):
        try:
            id_card_client = input("Introduceti ID-ul clientului: ")
            nume = input("Introduceti numele clientului: ")
            prenume = input("Introduceti prenumele clientului: ")
            cnp = int(input("Introduceti CNP-ul clientului: "))
            data_nasterii = input('Introduceti data nasterii (an, luna, ziua): ')
            year, month, day = map(int, data_nasterii.split('.'))
            date = datetime(year, month, day)
            data_inregistrarii = input('Introduceti data inregistrarii (an, luna, ziua): ')
            year, month, day = map(int, data_inregistrarii.split('.'))
            date = datetime(year, month, day)

            self.__client_service.adaugare(id_card_client, nume, prenume, cnp, data_nasterii, data_inregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_stergere_client(self):
        try:
            id_card_client = input("Dati ID-ul clientului care se sterge: ")

            self.__client_service.stergere(id_card_client)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modificare_client(self):
        try:
            id_card_client = input("Introduceti ID-ul clientului care se modifica: ")
            nume = input("Introduceti numele clientului: ")
            prenume = input("Introduceti prenumele clientului: ")
            cnp = int(input("Introduceti CNP-ul clientului: "))
            data_nasterii = input('Introduceti data nasterii (an, luna, ziua): ')
            year, month, day = map(int, data_nasterii.split('.'))
            date = datetime(year, month, day)
            data_inregistrarii = input('Introduceti data inregistrarii (an, luna, ziua): ')
            year, month, day = map(int, data_inregistrarii.split('.'))
            date = datetime(year, month, day)

            self.__client_service.modificare(id_card_client, nume, prenume, cnp, data_nasterii, data_inregistrarii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare_clienti(self):
        clienti = self.__client_service.get_all()
        for client in clienti:
            print(client)

    def run_crud_tranzactii(self):
        while True:
            print("1. Adaugare tranzactie")
            print("2. Stergere tranzactie")
            print("3. Modificare tranzactie")
            print("a. Afiseaza toate tranzactiile")
            print("x. Inapoi")
            option = input("Dati optiunea: ")
            if option == "1":
                self.ui_adaugare_tranzactie()
            elif option == "2":
                self.ui_stergere_tranzactie()
            elif option == "3":
                self.ui_modificare_tranzactie()
            elif option == "a":
                self.ui_afisare_tranzactie()
            elif option == "x":
                break
            else:
                print("Optiune invalida!")

    def ui_adaugare_tranzactie(self):
        try:
            id_tranzactie = input('Introduceti ID-ul tranzactiei: ')
            id_masina = input('Introduceti ID-ul masinii: ')
            id_card_client = input('Introduceti ID-ul cardului clientului: ')
            suma_piese = int(input('Introduceti suma pieselor: '))
            suma_manopera = int(input('Introduceti suma manoperei: '))
            data = input('Introduceti data (an, luna, ziua): ')
            year, month, day = map(int, data.split('.'))
            date = datetime(year, month, day)
            ora = input('Introduceti ora: ')

            self.__tranzactie_service.adaugare(id_tranzactie, id_masina, id_card_client, suma_piese, suma_manopera,
                                               data, ora)

            print('Tranzactia a fost adaugata.')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare_tranzactie(self):
        for tranzactie in self.__tranzactie_service.get_all():
            print(tranzactie)

    def ui_stergere_tranzactie(self):
        try:
            id_tranzactie = input('Introduceti ID-ul tranzactiei care se va sterge: ')
            self.__tranzactie_service.stergere(id_tranzactie)
            print('Tranzactia a fost stearsa.')
        except KeyError as ke:
            print(ke)

    def ui_modificare_tranzactie(self):
        try:
            id_tranzactie = input('Introduceti ID-ul tranzactiei de modificat: ')
            id_masina = input('Introduceti ID-ul masinii: ')
            id_card_client = input('Introduceti ID-ul cardului clientului: ')
            suma_piese = int(input('Introduceti suma pieselor: '))
            suma_manopera = int(input('Introduceti suma manoperei: '))
            data = input('Introduceti data (an, luna, ziua): ')
            year, month, day = map(int, data.split('.'))
            date = datetime(year, month, day)
            ora = input('Introduceti ora: ')

            self.__tranzactie_service.modificare(id_tranzactie, id_masina, id_card_client, suma_piese, suma_manopera,
                                                 data, ora)

            print('Tranzactia a fost modificata.')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def generare_random(self):
        n = int(input("Numarul de masini: "))
        lista_id = ['5', '7', '8']
        lista_model = ['model3', 'model4', 'model5', 'model6']
        lista_ani = ['2015', '2016', '2017', '2018']
        lista_km = ['100000', '200000']
        lista_garantie = ['da', 'nu']

        for i in range(n):
            try:
                id = random.choice(lista_id)
                model = random.choice(lista_model)
                an = random.choice(lista_ani)
                nr_km = random.choice(lista_km)
                garantie = random.choice(lista_garantie)
                self.__masina_service.adaugare(id, model, an, nr_km, garantie)
            except Exception as e:
                print(e)
                print("Una dintre masini exista deja.")



    def ui_merge_sort(self):
        array = self.__tranzactie_service.get_all()
        self.__tranzactie_service.merge_sort(array, 0, len(array) - 1, lambda tranzactieA, tranzactieB: tranzactieA.suma_manopera > tranzactieB.suma_manopera)
        for tranzactie in array:
            print(tranzactie.masina,", suma manopera:", tranzactie.suma_manopera)