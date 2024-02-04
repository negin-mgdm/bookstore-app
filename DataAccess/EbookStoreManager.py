# class used to harbour state and behavior used for storing and managing ebook records in the database.
class EbookStoreManager:

    def __init__(self, conn):
        self.conn = conn

#region insert
    # function to insert an ebook record into the database.
    def insert_book(self, ebook, startup = False):
        match = self.search_book_by_title(ebook[0])
        
        # don't insert record if it already exists.
        if(match is not None):
            if(not startup):
                print(f"Cannot add new record for ebook with title \'{ebook[0]}\' as it has been already added to the store.")
            return

        sql_insert_ebookstore_table = ''' INSERT INTO ebookstore(title, author, qty)
              VALUES(?,?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql_insert_ebookstore_table, ebook)
        self.conn.commit()
#endregion

#region search
    # function to search an ebook based on a given id.
    def search_book_by_id(self, id):
        sql_search_ebook = ''' SELECT * FROM ebookstore WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_ebook, (id,))
        self.conn.commit()
        return cur.fetchone()

    # function to search an ebook based on a given title.
    def search_book_by_title(self, title):
        sql_search_ebook = ''' SELECT * FROM ebookstore WHERE title = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_ebook, (title,))
        self.conn.commit()
        return cur.fetchone()

     # function to search an ebook based on a given author.
    def search_books_by_author(self, author):
        sql_search_ebook = ''' SELECT * FROM ebookstore WHERE author = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_search_ebook, (author,))
        self.conn.commit()
        return cur.fetchall()

     # function to fetch all available ebook records from the database. 
    def search_books(self):
        sql_search_ebook = ''' SELECT * FROM ebookstore'''
        cur = self.conn.cursor()
        cur.execute(sql_search_ebook)
        self.conn.commit()
        return cur.fetchall()
#endregion

#region update
    # function to update an ebook database record using its id.
    def update_ebook_by_id(self, ebook):
        record_id = ebook[0]
        match = self.search_book_by_id(record_id)
        
        # don't attempt an update if no match is found for the given record id.
        if(match is None):
            print(f"Cannot update the provided ebook with id: {record_id} as it doesn't already exist in the store.")
            return

        sql_insert_ebookstore_table = ''' UPDATE ebookstore 
            SET title = ?,
                author = ?,
                qty = ?
            WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_insert_ebookstore_table, (ebook[1], ebook[2], ebook[3], record_id))
        self.conn.commit()

    # function to update an ebook based on a given title.
    def update_ebook_by_title(self, ebook, title):
        match = self.search_book_by_title(title)
        if(match is None):
            print(f"Cannot update the provided ebook with title \'{title}\' as it doesn't already exist in the store.")
            return

        sql_insert_ebookstore_table = ''' UPDATE ebookstore 
            SET title = ?,
                author = ?,
                qty = ?
            WHERE title = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_insert_ebookstore_table, (ebook[0], ebook[1], ebook[2], title))
        self.conn.commit()

#endregion

#region delete
    # function to delete an ebook record based on a given id.
    def delete_book_by_id(self, id):
        match = self.search_book_by_id(id)

        # prevent an attempt to delete if given record id does not match an existing database entry.  
        if(match is None):
            print(f"Delete not needed for book with id \'{id}\' as it already doesn't exist in the store.")
            return

        sql_delete_ebookstore_table = ''' DELETE FROM ebookstore WHERE id = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_delete_ebookstore_table, (id,))
        self.conn.commit()

    # function to delete all existing ebook records in the database.
    def delete_all(self):
        sql_delete_ebookstore_table = ''' DELETE FROM ebookstore'''
        cur = self.conn.cursor()
        cur.execute(sql_delete_ebookstore_table)
        self.conn.commit()
    
    # function to delete an ebook based on a given book title.
    def delete_book_by_title(self, title):
        match = self.search_book_by_title(title)
        if(match is None):
            print(f"Delete not needed for book with title \'{title}\' as it already doesn't exist in the store.")
            return

        sql_delete_ebookstore_table = ''' DELETE FROM ebookstore WHERE title = ? '''
        cur = self.conn.cursor()
        cur.execute(sql_delete_ebookstore_table, (title,))
        self.conn.commit()
#endregion