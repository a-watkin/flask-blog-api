import os
import sqlite3


class Database(object):
    def __init__(self):
        # self.db_name = 'without_sql_alchemy.db'

        # having some issue with importing so, specifying the path to the db
        self.db_name = os.path.join(os.getcwd(), 'without_sql_alchemy.db')

    @classmethod
    def get_placeholders(cls, num):
        return ','.join(['?' for x in list(range(num))])

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

    def insert_data(self, **kwargs):
        # print('\nHello from insert_data, the **kwargs values are ', kwargs,
        #       'the db name is', self.db_name)
        """
        Expects any number of named arguments but must include a table name.

        db.insert_data(
        table='tag',
        tag_name=new_tag,
        user_id='28035310@N00'
        )
        """

        table_name = kwargs['table']
        del kwargs['table']

        data = [tuple(kwargs.values())]

        placeholders = self.get_placeholders(len(kwargs))

        try:
            with sqlite3.connect(self.db_name) as connection:
                query_string = ('INSERT INTO {} VALUES({})'.format(
                    table_name, placeholders), data)

                c = connection.cursor()
                c.executemany('INSERT INTO {} VALUES({})'.format(
                    table_name, placeholders), data)
        except Exception as e:
            print('insert_data problem ', e)

    def make_query(self, query_string):
        with sqlite3.connect(os.path.join(self.db_name)) as connection:
            c = connection.cursor()
            return [x for x in c.execute(query_string)]

    def get_row(self, table_name, id_name, id_value):
        q_data = None
        with sqlite3.connect(self.db_name) as connection:
            c = connection.cursor()
            c.row_factory = sqlite3.Row
            q_data = c.execute(
                '''
                SELECT * FROM {} WHERE {} = "{}"
                '''.format(
                    table_name, id_name, id_value
                )
            )

        return [dict(ix) for ix in q_data]

    def get_rows(self, table_name):
        q_data = None
        with sqlite3.connect(self.db_name) as connection:
            c = connection.cursor()
            c.row_factory = sqlite3.Row
            q_data = c.execute(
                '''
                SELECT * FROM {}
                '''.format(table_name))

        return [dict(ix) for ix in q_data]

    def get_query_as_list(self, query_string):
        q_data = None
        with sqlite3.connect(self.db_name) as connection:
            c = connection.cursor()
            c.row_factory = sqlite3.Row
            q_data = c.execute(query_string)

        return [dict(ix) for ix in q_data]


if __name__ == "__main__":
    db = Database()

    # print(os.path.join(os.getcwd(), db.db_name))

    # print(db.get_rows('post'))

    # db.make_db()

    # print(db.db_name)

    # print(db.get_query_as_list(
    #     '''
    #     SELECT * FROM post
    #     '''
    # ))

    # db.db_name = 'without_sql_alchemy.db'

    # db.make_db()

    # db.make_query(
    #     '''
    #     INSERT into user (username)
    #     VALUES ('test')
    #     '''
    # )

    # print(db.make_query(
    #     '''
    #     SELECT * from user
    #     '''
    # ))
