from Repository.file_repository import FileRepository
from Service.client_service import ClientService
from Tests.utils import clear_file


def test_add_client():
    clear_file("clienti_test.txt")
    clienti_repository = FileRepository("clienti_test.txt")
    service = ClientService(clienti_repository)
    service.adaugare('1', 'nume1', 'prenume1', 123456789012, '1999.11.11', '2020.11.11')
    assert len(service.get_all()) == 1
    added = clienti_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == 'nume1'
    assert added.prenume == 'prenume1'
    assert added.cnp == 123456789012
    assert added.data_nasterii == '1999.11.11'
    assert added.data_inregistrarii == '2020.11.11'

    try:
        service.adaugare('1', 'nume1', 'prenume1', 123456789012, '1999.11.11', '2020.11.11')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

def test_delete_client():
    clear_file("clienti_test.txt")
    clienti_repository = FileRepository("clienti_test.txt")
    service = ClientService(clienti_repository)
    service.adaugare('1', 'nume1', 'prenume1', 123456789012, '1999.11.11', '2020.11.11')

    try:
        service.stergere('2')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.stergere('1')
    assert len(service.get_all()) == 0

def test_update_client():
    clear_file("clienti_test.txt")
    clienti_repository = FileRepository("clienti_test.txt")
    service = ClientService(clienti_repository)
    service.adaugare('1', 'nume1', 'prenume1', 123456789012, '1999.11.11', '2020.11.11')
    service.modificare('1', 'nume2', 'prenume2', 123456789000, '1999.12.12', '2019.12.12')
    updated = clienti_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.nume == 'nume2'
    assert updated.prenume == 'prenume2'
    assert updated.cnp == 123456789000
    assert updated.data_nasterii == '1999.12.12'
    assert updated.data_inregistrarii == '2019.12.12'
