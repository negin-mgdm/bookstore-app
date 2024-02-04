import sqlite3

from DataAccess.EbookStoreManager import EbookStoreManager

# class used for general database interactions. 
class DatabaseManager:
    def __init__(self):   
        self.conn = self.setup_db()

# function used to create a table.
    def _create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Exception as e:
            print(e)

# function to create and populate required tables on startup. 
    def _build_tables_on_startup(self, conn):
        self._create_ebooks_table(conn)
        self._populate_ebooks_table_with_dummy_data(conn)

# function to create the ebooks table.
    def _create_ebooks_table(self, conn):
        # create ebooks table query
        sql_create_ebookstore_table = """ CREATE TABLE IF NOT EXISTS ebookstore (
                                            id integer PRIMARY KEY,
                                            title text NOT NULL,
                                            author text,
                                            qty integer
                                        ); """
        
        if conn is not None:
            # create ebooks table
             self._create_table(conn, sql_create_ebookstore_table)
        else:
            print("Error! cannot create the database connection.") 

# function to populate ebooks table with dummy data.
    def _populate_ebooks_table_with_dummy_data(self, conn):
        ebookstore_manager = EbookStoreManager(conn)

        ebooks = [
            ('A Tale of Two Cities', 'Charles Dickens', '30'),
            ('Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', '40'),
            ('The Lion, the Witch and the Wardrobe', 'C.S. Lewis', '25'),
            ('The Lord of the Rings', 'J.R.R. Tolkien', '37'),
            ('Alice in Wonderland', 'Lewis Carroll', '12'),
            ]
        for ebook in ebooks:
            ebookstore_manager.insert_book(ebook, True)
    
# function to create a database connection.    
    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Exception as e:
            print('Following error occurred while connecting to the local sqlite database.')
            print(e)

# function to close connection to the database.        
    def close_connection(self):
        self.conn.close()

# function to setup the database on application startup.
    def setup_db(self):
        database = r"database.db"

        # create a database connection
        conn = self.create_connection(database)
        
        # build required tables on startup
        self._build_tables_on_startup(conn)

        return conn
    