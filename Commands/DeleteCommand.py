from Commands.Command import Command

# class to capture user's delete commands.
class DeleteCommand(Command):
    def __init__(self, ebookstore_manager) -> None:
        super().__init__(ebookstore_manager)
    
    # function to handle user ebook deletions based on an id.
    def _delete_by_Id(self):
        record_id = input('Enter Id of ebook record to be deleted: ')
        self.ebookstore_manager.delete_book_by_id(record_id)

    # function to handle user ebook deletions based on a title.
    def _delete_by_title(self):
        title = input('Enter title of ebook to be deleted: ')
        ebook = self.ebookstore_manager.search_book_by_title(title)

        ebook_id = ebook[0]
        self.ebookstore_manager.delete_book_by_id(ebook_id)

    # function to handle user ebook deletions based on an author.
    def _delete_by_author(self):
        author = input('Enter author of ebook to be deleted: ')
        ebooks = self.ebookstore_manager.search_books_by_author(author)

        for ebook in ebooks:
            self.ebookstore_manager.delete_book_by_id(ebook[0])

    # function to handle a user's request to delete all ebook records.
    def _delete_all(self):
        self.ebookstore_manager.delete_all()
        print('All ebook records have been cleared.')

    # function to handle different types of deletion request by the user.
    def run(self):
        options = '''
1. Delete by Id
2. Delete by title
3. Delete by author
4. Delete all records
'''
        choice = int(input(options))
        match choice:
            case 1:
                self._delete_by_Id()
            case 2:
                self._delete_by_title()
            case 3:
                self._delete_by_author()
            case 4:
                self._delete_all()