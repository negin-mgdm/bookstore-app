from Commands.Command import Command

# class to capture update command by user 
class UpdateCommand(Command):
    def __init__(self, ebookstore_manager) -> None:
        super().__init__(ebookstore_manager)

    # function to handle user request to update an ebook record.
    def _update_book(self):
        user_input = input('''Enter a new book to be added. Provide the following details id, title, author and quantity. Please ensure a valid record id is supplied.
for example: 
3, A Tale of Two Cities, Charles Dickens, 30: ''')
        
        # split user's input based on the comma character and strip all splits of leading and trailing spaces.
        ebook = list(map(lambda x: x.strip(), user_input.split(',')))
        self.ebookstore_manager.update_ebook_by_id(ebook)

    # function acting as entry point to handle a user's ebook record update request. 
    def run(self):
        self._update_book()