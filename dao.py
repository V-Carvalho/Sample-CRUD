import sqlite3

# Connect to database
db = sqlite3.connect('example.db')
cursor = db.cursor()


class DAO:
    def create_database(self, ):
        # Creating table
        table = """CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY AUTOINCREMENT,username VARCHAR(255) NOT NULL, 
        password CHAR(25) NOT NULL); """
        db.execute(table)

    def insert_data(self, username, password):
        self.create_database()
        cursor.execute('INSERT INTO example (username, password) VALUES ( ?, ? );', (username, password))
        db.commit()
        return cursor.rowcount

    def select_data(self, username):
        self.create_database()
        if username == '*':
            data = cursor.execute('SELECT * FROM example')
        else:
            data = cursor.execute('SELECT * FROM example WHERE username = ?', (username,))
        return data

    def update_data(self, new_username, username):
        self.create_database()
        cursor.execute('UPDATE example SET username = ?  WHERE username = ?', (new_username, username))
        db.commit()
        return cursor.rowcount

    def delete_data(self, username):
        self.create_database()
        if username == '*':
            cursor.execute('DROP TABLE example')
            db.commit()
        else:
            cursor.execute('DELETE FROM example WHERE username = ?', (username,))
            db.commit()
        return cursor.rowcount

    def close_connection_database(self):
        db.close()
