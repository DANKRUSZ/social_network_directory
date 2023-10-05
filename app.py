from lib.database_connection import DatabaseConnection
from lib.account_repository import AccountRepository
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all artists
account_repository = AccountRepository(connection)
post_repository = PostRepository(connection)


for account in account_repository.all():
    print(account)

for post in post_repository.all():
    print(post)