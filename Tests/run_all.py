from Tests.test_tranzactie_service import test_add_tranzactie, test_delete_tranzactie, test_update_tranzactie
from Tests.test_domain import test_masina, test_client, test_tranzactie
from Tests.test_client_service import test_add_client, test_delete_client, test_update_client
from Tests.test_repository import  test_delete_repository, test_update_repository, test_add_repository
from Tests.test_masina_service import test_add_masina, test_delete_masina, test_update_masina

def run_all_tests():
    test_masina()
    test_client()
    test_tranzactie()

    test_add_repository()
    test_delete_repository()
    test_update_repository()

    test_add_masina()
    test_delete_masina()
    test_update_masina()

    test_add_client()
    test_delete_client()
    test_update_client()

    test_add_tranzactie()
    test_delete_tranzactie()
    test_update_tranzactie()