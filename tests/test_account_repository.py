from lib.account_repository import AccountRepository
from lib.account import Account


def test_get_all_accounts(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = AccountRepository(db_connection) # Create a new AccountRepository

    accounts = repository.all() # Get all accounts

    # Assert on the results
    assert accounts == [
        Account(1, 'dan@email.com', 'dan'),
        Account(2, 'harry@email.com', 'harry')
    ]


def test_get_single_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    account = repository.find(1)
    assert account == Account(1, 'dan@email.com', 'dan')


def test_create_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)

    repository.create(Account(None, "luke@email.com", "luke"))

    result = repository.all()
    assert result == [
        Account(1, 'dan@email.com', 'dan'),
        Account(2, 'harry@email.com', 'harry'),
        Account(3, 'luke@email.com', 'luke')
    ]


def test_delete_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = AccountRepository(db_connection)
    repository.delete(2) # Apologies to harry...

    result = repository.all()
    assert result == [
        Account(1, 'dan@email.com', 'dan')
    ]