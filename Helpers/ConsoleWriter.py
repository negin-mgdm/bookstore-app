# helper class to enable formatted console prints. 
class ConsoleWriter:
    
    # helper function to enable printing of an ebook record in a formatted manner.
    def print_book_info(self, ebook):
        print_message = f'''Id: \'{ebook[0]}\', Title: \'{ebook[1]}\', Author: \'{ebook[2]}\', Quantity: \'{ebook[3]}\''''
        print(print_message)