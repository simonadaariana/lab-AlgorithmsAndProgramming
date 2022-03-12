from Domain.add_operation import AddOperation
from Domain.masina import Masina

from Domain.masina_validator import MasinaValidator
from Repository.file_repository import FileRepository
from Service.undo_redo_service import UndoRedoService


class MasinaService:
    def __init__(self, masini_repository: FileRepository, masina_validator: MasinaValidator, undo_redo_service: UndoRedoService):
        self.__masini_repository = masini_repository
        self.__masina_validator = masina_validator
        self.__undo_redo_service = undo_redo_service

    def get_all(self):
        return self.__masini_repository.get_all()

    def adaugare(self, id_masina, model, an_achizitie, nr_km, garantie):

        masina = Masina(id_masina, model, an_achizitie, nr_km, garantie)
        self.__masina_validator.valideaza(masina)
        self.__masini_repository.adaugare(masina)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__masini_repository, masina))
        self.__undo_redo_service.add_to_redo(AddOperation(self.__masini_repository, masina))

    def stergere(self, id_masina):

        self.__masini_repository.stergere(id_masina)


    def modificare(self, id_masina, model, an_achizitie, nr_km, garantie):
        masina = self.__masini_repository.get_by_id(id_masina)
        if masina is None:
            raise KeyError(f"Nu exista deja o maisna cu id-ul {id_masina}")

        if model != "":
            masina.model = model
        if an_achizitie != 0:
            masina.an_achizitie = an_achizitie
        if nr_km != 0:
            masina.nr_km = nr_km
        if garantie != "":
            masina.garantie = garantie

        self.__masina_validator.valideaza(masina)

        self.__masini_repository.modificare(masina)