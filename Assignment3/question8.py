import csv
from tabulate import tabulate
class Library_Book_Management:
    def __init__(self):
        self.__book_title = None
        self.__author = None
        self.__genre = None
        self.__isbn = None
        self.__publisher = None
        self.__publication_year = None
        self.__edition = None
        self.__format = None
        self.__language = None
        self.__pages = None
        self.__status = None
    def ui(self):
        print(' _______________________________________________________\n')
        print('|                 1) library assistant                  \n|')
        print('|                 1) Student                            |')
        print('________________________________________________________')
    
    def book_list(self):
        with open('books.csv', 'r', newline="", encoding='utf-8') as file:
            reader = csv.reader(file)
            blist = list(reader)
            blist = list(filter(None, blist))
        print(tabulate(blist[0: ], headers=['Title', 'Author', 'Genre', 'ISBN', 'Publisher', 'Publication year',
                                            'Edition', 'Format', 'Language', 'Pages', 'Status'], tablefmt='fancy_grid'))
        
    def prompt_books_data(self):
        while True:
            self.__book_title = input('Book Title: ').strip()
            if self.__book_title: 
                break
            print('Error! Title of book cannot be empty.')

        self.__author = input('Author: ').strip()
        self.__genre = input('Genre: ').strip()
        self.__publisher = input('Publisher: ').strip()
        self.__edition = input('Edition: ').strip()
        self.__format = input('Format: ').strip()
        self.__language = input('Language: ').strip()
        self.__isbn = input('ISBN: ').strip()

        while True:
            try:
                self.__publication_year = int(input('Publication Year: '))
                break
        
            except ValueError:
                print('Error! Publication year must be digit.')
            except Exception as e:
                print(f'Error! {e}')

        while True:
            try:
                self.__pages = int(input('pages'))
                break

            except ValueError: 
                print('Error! Pages must be in digit.')
            except Exception as e:
                print(f'Error! {e}')


    def add_book(self):
        self.prompt_books_data()
        while True:
            try: 
                with open('books.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.wrightrow([self.__book_title, self.__author, self.__genre, self.__isbn, self.__publisher,
                                      self.__publication_year, self.__edition, self.__format, self.__language, self.__pages, self.__status])
                    
            except PermissionError:
                print('Error! you do not have permission to append in this file.')
            except Exception as e:
                print(f'Error! {e}')

    def issue_book(self):
    
    def return_book(self):
    
    def search_book(self):

class Libarian():
    def __init__(self, para_instance):
        self.lbm = para_instance
    def mainpage(self):
        self.libraian_ui()
        choice = input('Your Choice: ')
        if choice == '1': 
            self.lbm.add_book()
        if choice == '2': 
            self.add_book()
        if choice == '0':
            return

class Student():
    def __init__(self):
        pass
    def mainpage(self):
        self.student_ui()
        choice = input('Your choice: ')
        if choice == '1': 
            self.issue_book()
        if choice == '2': 
            self.return_book()
        if choice == '3': 
            self.search_book()
        if choice == '0':
            return 

lbm = Library_Book_Management()
choice = input('Your choice: ')
while True:
    if choice == '1':
        user = Libarian(lbm)
    if choice == '2': 
        user = Student(lbm)
    if choice == '0':
        break
    user.mainpage()
'''
class LibrarySystem:
    """Handles all book-related data operations."""
    def __init__(self):
        self.books_file = 'books.csv'

    def load_books(self):
        with open(self.books_file, 'r') as f:
            return list(csv.reader(f))

    def add_book(self, book_data):
        # Validation and CSV append logic here

    def search_book(self, query):
        # Search logic here

    # Other methods: issue_book, return_book, etc.

class Librarian:
    def __init__(self, library_system):
        self.library = library_system  # Composition

    def show_menu(self):
        print("1. Add Book\n2. List Books\n0. Exit")
        choice = input("Your choice: ")
        if choice == '1':
            self.library.add_book(...)

class Student:
    def __init__(self, library_system):
        self.library = library_system  # Composition

    def show_menu(self):
        print("1. Search Book\n2. Issue Book\n0. Exit")
        choice = input("Your choice: ")
        if choice == '1':
            self.library.search_book(...)

# Usage
lib_system = LibrarySystem()

user_type = input("Are you a (1) Librarian or (2) Student? ")
if user_type == '1':
    user = Librarian(lib_system)
elif user_type == '2':
    user = Student(lib_system)

user.show_menu()
'''