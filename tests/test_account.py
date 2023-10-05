from lib.account import Account

def test_account_constructs():
    account = Account(1, 'dan@email.com', 'dan')
    assert account.id == 1
    assert account.email_address == 'dan@email.com'
    assert account.username == 'dan'

def test_equality():
    account1 = Account(1, 'dan@email.com', 'dan')
    account2 = Account(1, 'dan@email.com', 'dan')
    assert account1 == account2

def test_format():
    account = Account(1, 'dan@email.com', 'dan')
    assert str(account) == 'Account(1, dan@email.com, dan)'