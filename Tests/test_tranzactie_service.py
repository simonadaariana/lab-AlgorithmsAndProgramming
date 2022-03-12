from Domain.client import Client
from Domain.masina import Masina
from Repository.file_repository import FileRepository
from Service.tranzactie_service import TranzactieService
from Tests.utils import clear_file


def test_add_tranzactie():
    clear_file("tranzactii_test.txt")
    tranzactii_repository = FileRepository("tranzactii_test.txt")
    clear_file("masini_test.txt")
    masini_repository = FileRepository("masini_test.txt")
    clear_file("clienti_test.txt")
    clienti_repository = FileRepository("clienti_test.txt")
    service = TranzactieService(tranzactii_repository, masini_repository, clienti_repository)
    masini_repository.adaugare(Masina('1', 'model1', 2016, 123456, 'da'))
    clienti_repository.adaugare(Client('1', 'nume1', 'prenume1', 123456789012, '1999.11.11', '2020.11.11'))
    service.adaugare('1', '1', '1', 500, 200, '2020.10.10', '15')
    assert len(service.get_all()) == 1
    added = tranzactii_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.id_masina == '1'
    assert added.id_card_client == '1'
    assert added.suma_piese == 500
    assert added.suma_manopera == 200
    assert added.data == '2020.10.10'
    assert added.ora == '15'


def test_delete_tranzactie():
    clear_file("tranzactii_test.txt")
    tranzactii_repository = FileRepository("tranzactii_test.txt")
    clear_file("masini_test.txt")
    masini_repository = FileRepository("masini_test.txt")
    clear_file("clienti_test.txt")
    clienti_repository = FileRepository("clienti_test.txt")
    service = TranzactieService(tranzactii_repository, masini_repository, clienti_repository)
    masini_repository.adaugare(Masina('1', 'model1', 2016, 123456, 'da'))
    clienti_repository.adaugare(Client('1', 'nume1', 'prenume1', 123456789012, '1999.11.11', '2020.11.11'))
    service.adaugare('1', '1', '1', 500, 200, '2020.10.10', '15')

    try:
        service.stergere('2')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.stergere('1')
    assert len(service.get_all()) == 0

def test_update_tranzactie():
    clear_file("tranzactii_test.txt")
    tranzactii_repository = FileRepository("tranzactii_test.txt")
    clear_file("masini_test.txt")
    masini_repository = FileRepository("masini_test.txt")
    clear_file("clienti_test.txt")
    clienti_repository = FileRepository("clienti_test.txt")
    service = TranzactieService(tranzactii_repository, masini_repository, clienti_repository)
    masini_repository.adaugare(Masina('1', 'model1', 2016, 123456, 'da'))
    clienti_repository.adaugare(Client('1', 'nume1', 'prenume1', 123456789012, '1999.11.11', '2020.10.10'))
    service.adaugare('1', '1', '1', 500, 200, '10.10.2020', '15')

    service.modificare('1', '1', '1', 500, 200, '2020.10.10', '15')
    updated = tranzactii_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.id_masina == '1'
    assert updated.id_card_client == '1'
    assert updated.suma_piese == 500
    assert updated.suma_manopera == 200
    assert updated.data == '2020.10.10'
    assert updated.ora == '15'

