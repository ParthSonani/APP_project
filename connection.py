import sqlite3
from sqlite3 import Error
#from Json_TO_Sql import TableCreation

class Connection:
    #TableCreation = TableCreation()
    conn = None
    count = 0

    @staticmethod
    def get_connection():
        """ create a database connection to a SQLite database """
        db_file = 'flight.db'
        if(Connection.count == 0):
            try:
                Connection.conn = sqlite3.connect(db_file)
                print(sqlite3.version)
                print("Database " + db_file + " created successfully !!!!")

            except Error as e:
                print(e)

            return Connection.conn
        else:
            return Connection.conn