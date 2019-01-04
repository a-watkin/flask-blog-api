import unittest

from .model.blog_db import Database
from .post import Post


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(
            'testuser',
            'password'
        )

        self.user.set_new_user()

    def tearDown(self):
        self.db = Database()
        self.db.make_query(
            '''
            DELETE FROM user WHERE username = "{}"
            '''.format('testuser')
        )

    def test_check_username(self):
        self.assertTrue(
            self.user.check_username()
        )

    def test_check_password(self):
        self.assertTrue(
            self.user.check_password()
        )


if __name__ == "__main__":
    pass
    # TestUser.insert_user_data()
    # InsertDummyData.remove_user_data()
