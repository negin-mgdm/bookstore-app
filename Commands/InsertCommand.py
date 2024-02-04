from Commands.Command import Command

# class to capture request command to add new ebook entries to the database.
class InsertCommand(Command):
    def __init__(self, ebookstore_manager) -> None:
        super().__init__(ebookstore_manager)

    # function to add new ebook record to the database.
    def _enter_book(self):
        user_input = input('''Enter a new book to be added. Provide the following details title, author and quantity.
for example: 
A Tale of Two Cities, Charles Dickens, 30:''')
        
        # split user's input based on the comma character and strip all splits of leading and trailing spaces.
        ebook = list(map(lambda x: x.strip(), user_input.split(',')))
        self.ebookstore_manager.insert_book(ebook)
    
    # function acting as an entry point to handling user's command request.
    def run(self):
        self._enter_book()