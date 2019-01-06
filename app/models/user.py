import os
import sys

from werkzeug.security import generate_password_hash, check_password_hash

try:
    from blog_db import Database
except Exception as e:
    sys.path.append(os.path.join(os.getcwd()))
    from app.blog_db import Database


class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.db = Database()

    def get_password_hash(self, password):
        return generate_password_hash(password)

    def verify_password(self, password_hash, password):
        return check_password_hash(password_hash, password)

    def check_username(self):
        print('check_username called')
        """
        Checks if the username is in the database.
        """
        db_resp = self.db.get_row('user', 'username', self.username)
        if db_resp is None:
            return False
        return True

    def check_password(self):
        hashed_password = self.db.get_query_as_list(
            '''
            SELECT hash FROM user WHERE username = "{}"
            '''.format(self.username)
        )
        if hashed_password is not None:
            print(hashed_password)
            return self.verify_password(
                hashed_password[0]['hash'], self.password
            )
        else:
            return False

    def check_credentials(self):
        if self.check_username and self.check_password():
            return True
        return False

    def set_password(self):
        hashed_password = self.get_password_hash(self.password)

        self.db.make_query(
            '''
            UPDATE user
            SET hash = "{}"
            WHERE username = "{}"
            '''.format(hashed_password, self.username)
        )

    def set_new_user(self):
        hashed_password = self.get_password_hash(self.password)

        self.db.insert_data(
            table='user',
            username=self.username,
            hash=hashed_password
        )


if __name__ == "__main__":
    u = User('test1', 'test1')
    # u.set_new_user()

    # u1 = User('test2', 'test2')
    # u1.set_new_user()

    # print(u.set_new_user())
    # print(u.check_credentials())

    print()
