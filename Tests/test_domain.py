from Domain.tranzactie import Tranzactie
from Domain.client import Client
from Domain.masina import Masina

def test_masina():
    masina = Masina('1', 'model1', 2015, 123456, 'da')
    assert masina.id_entitate == '1'
    assert masina.model == 'model1'
    assert masina.an_achizitie == 2015
    assert masina.nr_km == 123456
    assert masina.garantie == 'da'


def test_client():
    client = Client('1', 'nume1', 'prenume1', 123456789012, '1999.11.11', '2020.11.11')
    assert client.id_entitate == '1'
    assert client.nume == 'nume1'
    assert client.prenume == 'prenume1'
    assert client.cnp == 123456789012
    assert client.data_nasterii == '1999.11.11'
    assert client.data_inregistrarii == '2020.11.11'

def test_tranzactie():
    tranzactie = Tranzactie('1','1','1', 500, 200, '2020.11.11', '15')
    assert tranzactie.id_entitate == '1'
    assert tranzactie.id_masina == '1'
    assert tranzactie.id_card_client == '1'
    assert tranzactie.suma_piese == 500
    assert tranzactie.suma_manopera == 200
    assert tranzactie.data == '2020.11.11'
    assert tranzactie.ora == '15'
