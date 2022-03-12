from Domain.masina_validator import MasinaValidator
from Repository.file_repository import FileRepository
from Service.masina_service import MasinaService
from Service.undo_redo_service import UndoRedoService
from Tests.utils import clear_file


def test_add_masina():
    clear_file("service_test.txt")
    masini_repository = FileRepository("service_test.txt")
    masina_validator = MasinaValidator()
    masina_undo_redo = UndoRedoService()
    service = MasinaService(masini_repository, masina_validator, masina_undo_redo)

    service.adaugare('1', 'model1', 2016, 123456, 'da')
    assert len(service.get_all()) == 1
    added = masini_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.model == 'model1'
    assert added.an_achizitie == 2016
    assert added.nr_km == 123456
    assert added.garantie == 'da'

    try:
        service.adaugare('1', 'moedl1', 2016, 123456, 'da')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

def test_delete_masina():
    clear_file("service_test.txt")
    masini_repository = FileRepository("service_test.txt")
    masina_validator = MasinaValidator()
    masina_undo_redo = UndoRedoService()
    service = MasinaService(masini_repository, masina_validator, masina_undo_redo)
    service.adaugare('1', 'model1', 2016, 123456, 'da')
    service.adaugare('2', 'model2', 2015, 100000, 'nu')

    try:
        service.stergere('3')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False

    service.stergere('1')
    assert len(service.get_all()) == 1
    deleted = masini_repository.get_by_id('1')
    assert deleted is None
    remaining = masini_repository.get_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'
    assert remaining.model == 'model2'
    assert remaining.an_achizitie == 2015
    assert remaining.nr_km == 100000
    assert remaining.garantie == 'nu'

def test_update_masina():
    clear_file("service_test.txt")
    masini_repository = FileRepository("service_test.txt")
    masina_validator = MasinaValidator()
    masina_undo_redo = UndoRedoService()
    service = MasinaService(masini_repository, masina_validator, masina_undo_redo)
    service.adaugare('1', 'model1', 2016, 123456, 'da')
    service.adaugare('2', 'model2', 2015, 100000, 'nu')

    service.modificare('1', 'model3', 2017, 100000, 'da')
    updated = masini_repository.get_by_id('1')
    assert updated is not None
    assert updated.id_entitate == '1'
    assert updated.model == 'model3'
    assert updated.an_achizitie == 2017
    assert updated.nr_km == 100000
    assert updated.garantie == 'da'

    try:
        service.modificare('3', 'model3', 2020 , 500, 'da')
        assert False
    except KeyError:
        assert True
    except Exception:
        assert False
