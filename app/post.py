
import datetime

from model.blog_db import Database
from utils import get_id


class Post(object):
    def __init__(self, title=None, content=None, id=None):
        self.post_id = None
        self.title = title
        self.content = content
        self.date_posted = datetime.datetime.now()
        self.date_published = None
        self.db = Database()

        if self.post_id == None:
            self.post_id = get_id()

    def get_posts(self):
        data = self.db.get_rows('post')
        print(data)

    def get_post(self, post_id):
        data = self.db.get_row('post', 'post_id', post_id)

    def create_post(self):
        self.db.insert_data(
            table='post',
            post_id=self.post_id,
            username="testuser",
            title=self.title,
            content=self.content,
            date_posted=self.date_posted,
            date_published=self.date_published,
        )

    def update_post(self, post_id):
        """
        post_id shouldn't change.
        """

        if self.get_post(post_id):
            self.db.make_query(
                '''
                UPDATE post
                SET title = "{}", content = "{}", date_posted = "{}", date_published = "{}"
                WHERE post_id = {}
                '''.format(
                    self.title,
                    self.content,
                    self.date_posted,
                    self.date_published,
                    self.post_id
                )
            )
        else:
            return False

    def remove_post(self, post_id):
        self.db.make_query(
            '''
            DELETE FROM post WHERE post_id = "{}"; 
            '''.format(post_id)
        )

        if self.get_post(post_id):
            return False

        return True


if __name__ == "__main__":
    p = Post(
        title='test post 2',
        content='some other content',
    )

    p.create_post()

    # print(p.post_id, p.title, p.content, p.date_posted)

    # p.create_post()

    # print(p.get_post(9058375446))

    # print(p.get_posts())
