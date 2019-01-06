# try:
#     import os
#     import sys
#     from .utils import *
# except Exception as e:
#     print('problem ', e)
#     sys.path.append('/'.join(os.path.join(os.getcwd()).split('/')[:-1]))
#     print(sys.path)
# from utils import *

import os
import sys
import datetime

from app.blog_db import Database
from app.utils import get_id


class Post(object):
    def __init__(self, title=None, content=None):
        self.username = None
        self.title = title
        self.content = content
        self.date_posted = datetime.datetime.now()
        self.date_published = None
        self.post_id = get_id()
        self.db = Database()

    def get_posts(self):
        data = self.db.get_rows('post')
        print(data)

    def get_post(self, post_id):
        data = self.db.get_row('post', 'post_id', post_id)
        return data

    def create_post(self):
        print(self.db, type(self.db))
        # test says this is a tuple
        self.db.insert_data(
            table='post',
            username=self.username,
            title=self.title,
            content=self.content,
            date_posted=self.date_posted,
            date_published=self.date_published,
            post_id=self.post_id
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
    # print()
    # print(sys.path)

    # print(
    #     sys.path.append(os.path.join(os.getcwd()))
    # )
    # print()
    # print(sys.path)

    p = Post(
        title='test post 2',
        content='some other content'
    )

    print(
        p.username,
        p.title,
        p.content,
        p.date_posted,
        p.date_published,
        p.post_id
    )

    # print('post_id is: ', p.post_id, type(p.post_id))
    # p.post_id = get_id()
    # print('post_id is: ', p.post_id, type(p.post_id))

    # print(p.get_post(905837544))

    # print(p.post_id, p.title, p.content, p.date_posted)

    # p.create_post()

    # print(p.get_post(9058375446))

    # print(p.get_posts())
