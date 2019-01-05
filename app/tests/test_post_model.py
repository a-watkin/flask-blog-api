import unittest

from database import blog_db
from app.models.post import Post


class TestPost(unittest.TestCase):

    def setUp(self):
        self.p = Post(
            title='test post 1',
            content='some other content'
        )

        self.p.create_post()

    def tearDown(self):
        self.db = Database()
        self.db.make_query(
            '''
            DELETE FROM post WHERE title = "{}"
            '''.format('test post 1')
        )

    def test_remove_post(self):
        self.assertTrue(
            self.p.remove_post(self.p.post_id)
        )
