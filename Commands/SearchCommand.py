from Commands.Command import Command

# class to handle a user's request to search ebook records.
class SearchCommand(Command):
    def __init__(self, ebookstore_manager) -> None:
        super().__init__(ebookstore_manager)

    # function to fetch all ebook entries.
    def _search_all_books(self):
        ebooks = self.ebookstore_manager.search_books()

        # inform user if no records exist
        if len(ebooks) == 0:
            print('No ebook records found.')
            return

        print('Book records available:')

        # print ebook record info for each fetched entry. 
        for ebook in ebooks:
            self.console_writer.print_book_info(ebook)

    # function to fetch all ebooks' record info based on an author.
    def _search_books_by_author(self):
        user_input = input('''Enter a book author to search for.
for example: 
\'Charles Dickens\'''')
        ebooks = self.ebookstore_manager.search_books_by_author(user_input)

        if len(ebooks) == 0:
            print(f'Could not find any books with the specified author: \'{user_input}\'')
            return

        print(f'''Books found for author '\{user_input}\':''')

        for ebook in ebooks:
            self.console_writer.print_book_info(ebook)

    # function to fetch an ebook record info based on its title. 
    def _search_book_by_title(self):
        user_input = input('''Enter a book title to be found.
for example: 
\'A Tale of Two Cities\'''')
        ebook = self.ebookstore_manager.search_book_by_title(user_input)

        if ebook is None:
            print(f'Could not find any book with the specified title: \'{user_input}\'')
            return

        print(f'''Book record found with title \'{user_input}\':''')
        self.console_writer.print_book_info(ebook)

    # function used to handle all types of search command types.
    def run(self):
        options = '''
1. Fetch all books
2. Search by title
3. Search by author
'''
        choice = int(input(options))
        match choice:
            case 1:
                self._search_all_books()
            case 2:
                self._search_book_by_title()
            case 3:
                self._search_books_by_author()