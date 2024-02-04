from Commands.DeleteCommand import DeleteCommand
from Commands.InsertCommand import InsertCommand
from Commands.SearchCommand import SearchCommand
from Commands.UpdateCommand import UpdateCommand
from DataAccess.EbookStoreManager import EbookStoreManager

class UserInputs:

    def __init__(self, conn):
        self.ebookstore_manager = EbookStoreManager(conn)

#region insert
    def add_new_ebook_record(self):
        command = InsertCommand(self.ebookstore_manager)
        command.run()
#endregion

#region search
    def search_for_ebook_record(self):
        command = SearchCommand(self.ebookstore_manager)
        command.run()
#endregion

#region update
    def update_ebook_record(self):
        command = UpdateCommand(self.ebookstore_manager)
        command.run()
#endregion

#region delete
    def delete_ebook_record(self):
        command = DeleteCommand(self.ebookstore_manager)
        command.run()
#endregion