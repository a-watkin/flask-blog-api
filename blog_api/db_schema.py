import sqlite3


def create_database(db_name):

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS user(
            username TEXT PRIMARY KEY UNIQUE NOT NULL,
            hash TEXT NULL
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS post(
            post_id INT PRIMARY KEY UNIQUE NOT NULL,
            username TEXT NOT NULL,
            title TEXT,
            content TEXT,
            datetime_posted TEXT,
            datetime_published TEXT,
            FOREIGN KEY(username) REFERENCES user(username) ON DELETE CASCADE
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tag(
            tag_name TEXT NOT NULL UNIQUE, 
            username TEXT NOT NULL,
            posts INT,
            PRIMARY KEY (tag_name, username)
            FOREIGN KEY(username) REFERENCES user(username) ON DELETE CASCADE
        );
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS post_tag(
            post_id INT references post(post_id) ON UPDATE CASCADE,
            tag_name TEXT references tag(tag_name) ON UPDATE CASCADE,
            PRIMARY KEY (post_id, tag_name)
        );
        '''
    )


if __name__ == "__main__":
    create_database('without_sql_alchemy.db')
