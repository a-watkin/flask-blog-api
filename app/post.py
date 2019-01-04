
from model.blog_db import Database


class Post(object):
    def __init__(self):
        self.db = Database()

    def get_all_posts(self):
        data = self.db.get_rows('post')
        print(data)

    def get_post(self):
        data = self.db.get_row('post')
