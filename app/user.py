from werkzeug.security import generate_password_hash, check_password_hash
from model.blog_db import Database


class User(object):

    def __init__(self):
        self.db = Database()

    def get_password_hash(self, password):
        return generate_password_hash(password)

    def verify_password(self, password_hash, password):
        return check_password_hash(password_hash, password)


if __name__ == "__main__":
    u = User()
    print(u.get_password_hash('beans'))
    print(u.verify_password(
        'pbkdf2:sha256:50000$3yB6XOHP$f7f17c90a6989ac51805b772691bc3166373c06ce45b7d349b210f9795a9b787',
        'test'))
