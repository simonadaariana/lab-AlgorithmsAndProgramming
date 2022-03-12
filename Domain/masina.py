from Domain.entitate import Entitate


class Masina(Entitate):

    def __init__(self, id_masina, model, an_achizitie, nr_km, garantie):
        super().__init__(id_masina)
        self.__model = model
        self.__an_achizitie = an_achizitie
        self.__nr_km = nr_km
        self.__garantie = garantie

    def __str__(self):
        return f"ID: {self.id_entitate}, model: {self.model}, an achizitie: {self.an_achizitie}, " \
                f"nr. km: {self.nr_km}, garantie: {self.garantie}"

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model_nou):
        self.__model = model_nou

    @property
    def an_achizitie(self):
        return self.__an_achizitie

    @an_achizitie.setter
    def an_achizitie(self, an_achizitie_nou):
        self.__an_achizitie = an_achizitie_nou

    @property
    def nr_km(self):
        return self.__nr_km

    @nr_km.setter
    def nr_km(self, nr_km_nou):
        self.__nr_km = nr_km_nou

    @property
    def garantie(self):
        return self.__garantie

    @garantie.setter
    def garantie(self, garantie_noua):
        self.__garantie = garantie_noua
