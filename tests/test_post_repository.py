from lib.post import Post
from lib.post_repository import PostRepository

def test_get_all_posts(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new AccountRepository

    posts = repository.all() # Get all accounts

    # Assert on the results
    assert posts == [
        Post(1, 'My Title 1', 'Content 1', 0, 1),
        Post(2, 'My Title 2', 'Content 2', 0, 2)
    ]


def test_get_single_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(1)
    assert post == Post(1, 'My Title 1', 'Content 1', 0, 1)


def test_create_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 'My Title 3', 'Content 3', 0, 1))

    result = repository.all()
    assert result == [
        Post(1, 'My Title 1', 'Content 1', 0, 1),
        Post(2, 'My Title 2', 'Content 2', 0, 2),
        Post(3, 'My Title 3', 'Content 3', 0, 1)
    ]


def test_delete_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(2) # Apologies to harry...

    result = repository.all()
    assert result == [
        Post(1, 'My Title 1', 'Content 1', 0, 1)
    ]