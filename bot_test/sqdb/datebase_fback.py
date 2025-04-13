import sqlite3

class FEED:
    def __init__(self, db_name='FEEDBACK.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.__create_tables__()

    def __create_tables__(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS feed
                            (fadb TEXT, 
                            name TEXT,
                            MARK TEXT)''')

    def fd(self, fadb, name, MARK):
        self.cursor.execute('''INSERT INTO feed (fadb, name, MARK) VALUES (?, ?, ?)''',
        (fadb, name, MARK))
        self.conn.commit()
    def fd_get(self): 
        self.cursor.execute('''SELECT * FROM feed''') 
        return self.cursor.fetchall()



