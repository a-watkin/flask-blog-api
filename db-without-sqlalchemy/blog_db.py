import sqlite3


class Database(object):
    def __init__(self, db_name=None):
        self.db = db_name

    @classmethod
    def make_db(cls, name):
        from db_schema import create_database
        # db_schema.create_database(name)
        create_database(name)
        cls.db_name = name
        if os.path.isfile(name):
            return True
        else:
            print('Database not created.')
            return False

    @classmethod
    def delete_database(cls):
        if cls.db_name in os.listdir():
            try:
                os.remove(cls.db_name)
                cls.db_name = None
                return True
            except OSError as e:
                print('Problem: ', e)
        else:
            print('Database not found')
            return False

    def make_query(self, query_string):
        with sqlite3.connect(self.db_name) as connection:
            c = connection.cursor()
            # print(query_string)
            return [x for x in c.execute(query_string)]


def main():
    db = Database()
    db.db_name = 'without_sql_alchemy.db'
