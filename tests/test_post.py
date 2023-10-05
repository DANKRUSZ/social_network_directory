from lib.post import Post

def test_constructs():
    post = Post(1, 'My Title 1', 'Content 1', 0, 1)
    assert post.id == 1
    assert post.title == 'My Title 1'
    assert post.content == "Content 1"
    assert post.views == 0
    assert post.account_id == 1

def test_equality():
    post1 = Post(1, 'My Title 1', 'Content 1', 0, 1)
    post2 = Post(1, 'My Title 1', 'Content 1', 0, 1)
    assert post1 == post2

def test_format():
    post = Post(1, 'My Title 1', 'Content 1', 0, 1)
    assert str(post) == 'Post(1, My Title 1, Content 1, 0, 1)'
