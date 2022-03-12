from copy import deepcopy

import jsonpickle as jsonpickle

from Domain.entitate import Entitate


class FileRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__storage = {}

    def __read_file(self):
        try:
            with open (self.__file_name,'r') as fp:
                self.__storage = jsonpickle.decode(fp.read())
        except :
            self.__storage={}

    def __write_to_file(self):
        with open(self.__file_name,'w') as fp:
            fp.write(jsonpickle.encode(self.__storage))

    def get_all(self):
        self.__read_file()
        return deepcopy(list(self.__storage.values()))

    def get_by_id(self, id_entitate):
        self.__read_file()
        if id_entitate in self.__storage:
            return deepcopy(self.__storage[id_entitate])
        return None

    def adaugare(self, entitate: Entitate):
        if self.get_by_id(entitate.id_entitate):
            raise KeyError(f"Exista deja o entitate cu id-ul {entitate.id_entitate}")

        self.__storage[entitate.id_entitate] = entitate
        self.__write_to_file()

    def stergere(self, id_entitate):

        if self.get_by_id(id_entitate) is None:
            raise KeyError(f"Nu exista nicio entitate cu id-ul {id_entitate}")
        del self.__storage[id_entitate]
        self.__write_to_file()

    def modificare(self, entitate: Entitate):
        if self.get_by_id(entitate.id_entitate) is None:
            raise KeyError(f"Nu exista nicio entitate cu id-ul {entitate.id_entitate}")

        self.__storage[entitate.id_entitate] = entitate
        self.__write_to_file()


