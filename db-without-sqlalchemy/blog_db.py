import os
import sqlite3


class Database(object):
    def __init__(self, db_name=None):
        self.db_name = db_name

    def make_db(self):
        from db_schema import create_database
        # db_schema.create_database(name)
        create_database(self.db_name)
        if os.path.isfile(self.db_name):
            return True
        else:
            print('Database not created.')
            return False

    def delete_database(self):
        if self.db_name in os.listdir():
            try:
                os.remove(self.db_name)
                self.db_name = None
                return True
            except OSError as e:
                print('Problem: ', e)
        else:
            print('Database not found')
            return False

    def make_query(self, query_string):
        with sqlite3.connect(os.path.join(self.db_name)) as connection:
            c = connection.cursor()
            # print(query_string)
            return [x for x in c.execute(query_string)]


if __name__ == "__main__":
    db = Database()
    db.db_name = 'without_sql_alchemy.db'

    db.make_db()

    # print(db.make_query(
    #     '''
    #     SELECT * from user
    #     '''
    # ))
