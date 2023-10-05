from lib.account import Account

class AccountRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from accounts')
        accounts = []
        for row in rows:
            item = Account(row["id"], row["email_address"], row["username"])
            accounts.append(item)
        return accounts

    def find(self, account_id):
        rows = self.connection.execute(
            'SELECT * from accounts WHERE id = %s', [account_id])
        row = rows[0]
        return Account(row["id"], row["email_address"], row["username"])

    def create(self, account):
        self.connection.execute('INSERT INTO accounts (email_address, username) VALUES (%s, %s)', [
            account.email_address, account.username])
        return None

    def delete(self, account_id):
        self.connection.execute(
            'DELETE FROM accounts WHERE id = %s', [account_id])
        return None