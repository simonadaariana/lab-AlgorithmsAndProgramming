class MasinaViewModel:
    def __init__(self, id_masina, model, an_achizitie, nr_km, garantie):
        self.id_masina = id_masina
        self.model = model
        self.an_achizitie = an_achizitie
        self.nr_km = nr_km
        self.garantie = garantie

    def __str__(self):
        return f'ID masina:{self.id_masina}, model: {self.model}, an_achizitie: {self.an_achizitie}, numar kilometri: {self.nr_km}, garantie: {self.garantie} '