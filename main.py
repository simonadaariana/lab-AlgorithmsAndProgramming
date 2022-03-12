from Domain.masina_validator import MasinaValidator
from Service.functionalitati import Functionalitati
from Service.tranzactie_service import TranzactieService
from Service.client_service import ClientService
from Service.masina_service import MasinaService
from Service.undo_redo_service import UndoRedoService
from Tests.run_all import run_all_tests
from UI.console import Consola
from Repository.file_repository import FileRepository

def main():

    masini_repository = FileRepository('masini.txt')
    masina_validator = MasinaValidator()
    clienti_repository = FileRepository('clienti.txt')
    tranzactii_repository = FileRepository('tranzactii.txt')

    undo_redo_service = UndoRedoService()
    masina_service = MasinaService(masini_repository, masina_validator, undo_redo_service)
    client_service = ClientService(clienti_repository)
    tranzactie_service = TranzactieService(tranzactii_repository, masini_repository, clienti_repository)
    functionalitati = Functionalitati(tranzactii_repository, masini_repository, clienti_repository)

    console = Consola(masina_service, client_service, tranzactie_service, functionalitati, undo_redo_service)
    console.run_menu()

run_all_tests()
main()