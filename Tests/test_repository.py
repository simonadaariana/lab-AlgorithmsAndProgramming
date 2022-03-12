from Domain.masina import Masina
from Repository.file_repository import FileRepository
from Tests.utils import clear_file


def test_add_repository():
    clear_file("repository_test.txt")
    entitati_repository = FileRepository("repository_test.txt")

    masina1 = Masina('1',2, 'ridicat', 'da', 'aaa')

    entitati_repository.adaugare(masina1)
    assert len(entitati_repository.get_all()) == 1
    added = entitati_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.model == 2
    assert added.an_achizitie == 'ridicat'
    assert added.nr_km == 'da'
    assert added.garantie == 'aaa'

    try:
        masina2 = Masina('1', 2, 'ridicat', 'da', 'aaa')
        entitati_repository.adaugare(masina2)
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

def test_delete_repository():
    clear_file("repository_test.txt")
    entitati_repository = FileRepository("repository_test.txt")
    masina1 = Masina('1', 'model1', 2016, 123456, 'da')
    masina2 = Masina('2', 'model2', 2015, 100000, 'nu')
    entitati_repository.adaugare(masina1)
    entitati_repository.adaugare(masina2)

    try:
        entitati_repository.stergere('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    entitati_repository.stergere('1')
    assert len(entitati_repository.get_all()) == 1
    deleted = entitati_repository.get_by_id('1')
    assert deleted is None
    remaining = entitati_repository.get_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.model == 'model2'
    assert remaining.an_achizitie == 2015
    assert remaining.nr_km == 100000
    assert remaining.garantie == 'nu'

def test_update_repository():
    clear_file("repository_test.txt")
    entitati_repository = FileRepository("repository_test.txt")
    masina1 = Masina('1', 'model1', 2016, 123456, 'da')
    masina2 = Masina('2', 'model2', 2015, 100000, 'nu')
    entitati_repository.adaugare(masina1)
    entitati_repository.adaugare(masina2)

    masina1 = Masina('1', 'model1', 2016 , 123456, 'da')
    entitati_repository.modificare(masina1)
    updated = entitati_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.model == 'model1'
    assert updated.an_achizitie == 2016
    assert updated.nr_km == 123456
    assert updated.garantie == 'da'
