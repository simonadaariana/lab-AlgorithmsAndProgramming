class MasinaValidator:
    def valideaza(self, masina):
        erori = []
        if masina.garantie not in ["da", "nu"]:
            erori.append("Garantia masinii trebuie sa aiba valorile 'da' sau 'nu'")
        if len(erori) > 0:
            raise ValueError(erori)