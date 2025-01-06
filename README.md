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


 
