import datetime
from collections import defaultdict

try:
    """
    Running as flask app.
    """
    from .blog_db import Database
    from .utils import get_id
except Exception as e:
    """
    Running as module.
    """
    print('\nRunning as a module, for testing\n')
    import os
    import sys

    sys.path.append(os.getcwd())
    from utils import get_id
    from blog_db import Database


class Post(object):
    def __init__(self, *args, **kwargs):
        # args contains the dictionary/JSON within a tuple
        # JSON or a dict works ok
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])

        # Here incase of instantiating the class with names arguments
        for key in kwargs:
            print(key, kwargs[key])
            setattr(self, key, kwargs[key])

        # default values if not present in args or kwargs
        if not hasattr(self, 'post_id'):
            self.post_id = get_id()

        if not hasattr(self, 'username'):
            self.username = 'a'

        if not hasattr(self, 'datetime_posted'):
            self.datetime_posted = datetime.datetime.now()

        if not hasattr(self, 'datetime_published'):
            self.datetime_published = datetime.datetime.now()

        # database connection
        self.db = Database()

    def __repr__(self):
        pass

    def __str__(self):
        return f'''
        A blog post: \n
        post_id: {self.post_id}\n
        title: {self.title}\n
        content: {self.content}\n
        datetime_posted: {self.datetime_posted}\n
        datetime_published: {self.datetime_published}\n
        '''

    def get_posts(self):
        data = self.db.get_rows('post')
        return data

    def get_post(self, post_id):
        print('get_post, ', post_id)
        # this query is returning an empty list
        data = self.db.get_row('post', 'post_id', post_id)
        print('get_post data, ', data)
        return data

    def create_post(self):
        print(self.db, type(self.db))
        # test says this is a tuple
        self.db.insert_data(
            table='post',
            post_id=self.post_id,
            username=self.username,
            title=self.title,
            content=self.content,
            datetime_posted=self.datetime_posted,
            datetime_published=self.datetime_published
        )

    def update_post(self, post_id):
        # these values are ok
        print('update_post, ',
              post_id,
              self.title,
              self.content,
              self.datetime_posted,
              self.datetime_published,
              self.post_id)

        # post_id shouldn't change.
        if self.get_post(post_id):
            print('getting this far?')
            self.db.make_query(
                '''
                UPDATE post
                SET title = "{}", content = "{}", datetime_posted = "{}", datetime_published = "{}"
                WHERE post_id = {}
                '''.format(
                    self.title,
                    self.content,
                    self.datetime_posted,
                    self.datetime_published,
                    self.post_id
                )
            )

            return True
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
    p = Post(title='test')
    p = Post(
        title='hello world',
        content='some rambling nonsense probably'
    )
    print(p)

    # print(p.get_posts())
