from lib.post import Post

class PostRepository:
    
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row["views"], row["account_id"])
            posts.append(item)
        return posts
    
    def find(self, post_id):
        rows = self.connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"], row["views"], row["account_id"])
    
    def create(self, post):
        self.connection.execute('INSERT INTO posts (title, content, views, account_id) VALUES (%s, %s, %s, %s)', [
            post.title, post.content, post.views, post.account_id])
        return None
    
    def delete(self, post_id):
        self.connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id])
        return None