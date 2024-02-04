from DataAccess.DatabaseManager import DatabaseManager
from UserInputHandler.UserInputs import UserInputs

# main entry point of the application.
def main():
    # setup db access.
    db_manager = DatabaseManager()

    # repeatedly ask for user commands by use of a main menu.
    while True:
        options = '''
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
'''
        choice = int(input(options))

        user_input_handler = UserInputs(db_manager.conn)
        match (choice):
            case 1:
                user_input_handler.add_new_ebook_record()                
            case 2:
                user_input_handler.update_ebook_record()
            case 3:
                user_input_handler.delete_ebook_record()
            case 4:
                user_input_handler.search_for_ebook_record()
            case 0:
                break
    
    # close db connection upon application termination.
    db_manager.close_connection()
    exit()

main()


