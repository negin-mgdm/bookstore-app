# Ebook Store Management System

## Overview
The Ebook Store Management System is a Python-based application that allows bookstore clerks to manage book records in a SQLite database. This project demonstrates CRUD (Create, Read, Update, Delete) operations through a command-line interface. It leverages object-oriented principles to ensure modularity and scalability.

## Features
- **Add New Books** – Enter new book records into the database.
- **Update Book Records** – Modify existing book information by ID.
- **Delete Books** – Remove book records by ID, title, author, or delete all records.
- **Search for Books** – Search book records by title, author, or list all books.
- **Formatted Output** – Book records are displayed in a structured format.
- **Persistent Storage** – Book records are stored in a SQLite database (`database.db`).

## Project Structure
```
├── main.py                     # Main entry point of the application
├── settings.json               # Configuration settings
│
├── DataAccess                  # Handles database interactions
│   ├── DatabaseManager.py      # Sets up and manages the database connection
│   ├── EbookStoreManager.py    # Manages ebook records in the database
│
├── Commands                    # Command classes for CRUD operations
│   ├── Command.py              # Base class for commands
│   ├── InsertCommand.py        # Handles inserting new book records
│   ├── UpdateCommand.py        # Handles updating book records
│   ├── DeleteCommand.py        # Handles deleting book records
│   ├── SearchCommand.py        # Handles searching for book records
│
├── Helpers                     # Utility/helper classes
│   ├── ConsoleWriter.py        # Formats and prints book records to the console
│
├── UserInputHandler            # Manages user input
│   ├── UserInputs.py           # Routes user input to the appropriate commands
```

## How It Works
Upon launching the application, users interact with a command-line menu to perform various operations on book records stored in the database. The project employs a modular structure with classes dedicated to handling different types of operations (insertion, search, update, and deletion).

### Database Structure
- **Database Name**: `ebookstore`
- **Table**: `book`
- **Columns**:  
  - `id` – Unique identifier for each book  
  - `title` – Title of the book  
  - `author` – Author's name  
  - `qty` – Quantity in stock  

### Initial Data
The database is populated with the following records during setup:  
| ID   | Title                                   | Author                 | Quantity |  
|------|-----------------------------------------|------------------------|----------|  
| 3001 | A Tale of Two Cities                     | Charles Dickens        | 30       |  
| 3002 | Harry Potter and the Philosopher's Stone | J.K. Rowling           | 40       |  
| 3003 | The Lion, the Witch and the Wardrobe     | C.S. Lewis             | 25       |  
| 3004 | The Lord of the Rings                    | J.R.R. Tolkien         | 37       |  
| 3005 | Alice in Wonderland                      | Lewis Carroll          | 12       |  
 
## Installation and Setup
1. **Clone the Repository**
   Clone the project from GitHub to your local machine:
    ```bash
    git clone https://github.com/negin-mgdm/bookstore-app.git
    cd bookstore-app
    ```
2. **Set Up a Virtual Environment**
   Ensure Python 3 and SQLite3 are installed.
   Create and activate a virtual environment to manage dependencies:
   # On Windows
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
   # On macOS/Linux
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**
   Ensure you have all required Python packages installed:
   ```
   pip install -r requirements.txt
   ```
4. **Run the Application**
   Start the application by running:
   ```
   python main.py
   ```
5. **Database Initialization**
   The database (database.db) will be automatically created and populated upon the first run of the application.

   




 
