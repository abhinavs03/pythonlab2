class LibraryManager:
    def __init__(self):
        self.books = {}

    def add_book(self, isbn, title, author, publisher, volume, year, isbn_number):
        if isbn in self.books:
            print(f"Book with ISBN {isbn} already exists.")
            return
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year,
            'isbn': isbn_number
        }
        print(f"Book '{title}' added successfully.")

    def remove_book(self, isbn):
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} does not exist.")
            return
        removed_book = self.books.pop(isbn)
        print(f"Book '{removed_book['title']}' removed successfully.")

    def get_book(self, isbn):
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} does not exist.")
            return
        book = self.books[isbn]
        for key, value in book.items():
            print(f"{key.capitalize()}: {value}")

    def search_books(self, query, search_by="title"):
        results = []
        for book in self.books.values():
            if query.lower() in book[search_by].lower():
                results.append(book)
        return results

    def list_books(self):
        if not self.books:
            print("No books currently in the library.")
            return
        for isbn, book in self.books.items():
            print(f"ISBN: {isbn}")
            for key, value in book.items():
                print(f"  {key.capitalize()}: {value}")

    def update_book(self, isbn, **kwargs):
        if isbn not in self.books:
            print(f"Book with ISBN {isbn} does not exist.")
            return
        self.books[isbn].update(kwargs)
        print(f"Book with ISBN {isbn} updated successfully.")

    def is_available(self, isbn):
        return isbn in self.books

def create_sample_library():
    manager = LibraryManager()
    sample_books = [
        ("1234567890", "Operating Systems", "Author A", "Publisher X", 1, 2021, "1234567890"),
        ("2345678901", "Data Structures", "Author B", "Publisher Y", 1, 2022, "2345678901"),
        ("3456789012", "Machine Learning", "Author C", "Publisher Z", 1, 2023, "3456789012"),
    ]
    for book in sample_books:
        manager.add_book(*book)
    return manager

if __name__ == "__main__":
    library_manager = create_sample_library()
    
    print("\nListing all books:")
    library_manager.list_books()
    
    print("\nRetrieving details of a book with ISBN 1234567890:")
    library_manager.get_book("1234567890")
    
    print("\nSearching for books by title 'Data Structures':")
    search_results = library_manager.search_books("Data Structures", search_by="title")
    for result in search_results:
        print(result)
    
    print("\nUpdating the details of a book with ISBN 1234567890:")
    library_manager.update_book("1234567890", title="Advanced Operating Systems", author="Author A+")
    library_manager.get_book("1234567890")
    
    print("\nChecking if a book with ISBN 1234567890 is available:")
    print(library_manager.is_available("1234567890"))
    
    print("\nRemoving a book with ISBN 1234567890:")
    library_manager.remove_book("1234567890")
    library_manager.list_books()


'''
Book 'Operating Systems' added successfully.
Book 'Data Structures' added successfully.
Book 'Machine Learning' added successfully.

Listing all books:
ISBN: 1234567890
  Title: Operating Systems
  Author: Author A
  Publisher: Publisher X
  Volume: 1
  Year: 2021
  Isbn: 1234567890
ISBN: 2345678901
  Title: Data Structures
  Author: Author B
  Publisher: Publisher Y
  Volume: 1
  Year: 2022
  Isbn: 2345678901
ISBN: 3456789012
  Title: Machine Learning
  Author: Author C
  Publisher: Publisher Z
  Volume: 1
  Year: 2023
  Isbn: 3456789012

Retrieving details of a book with ISBN 1234567890:
Title: Operating Systems
Author: Author A
Publisher: Publisher X
Volume: 1
Year: 2021
Isbn: 1234567890

Searching for books by title 'Data Structures':
{'title': 'Data Structures', 'author': 'Author B', 'publisher': 'Publisher Y', 'volume': 1, 'year': 2022, 'isbn': '2345678901'}

Updating the details of a book with ISBN 1234567890:
Book with ISBN 1234567890 updated successfully.
Title: Advanced Operating Systems
Author: Author A+
Publisher: Publisher X
Volume: 1
Year: 2021
Isbn: 1234567890

Checking if a book with ISBN 1234567890 is available:
True

Removing a book with ISBN 1234567890:
Book 'Advanced Operating Systems' removed successfully.
ISBN: 2345678901
  Title: Data Structures
  Author: Author B
  Publisher: Publisher Y
  Volume: 1
  Year: 2022
  Isbn: 2345678901
ISBN: 3456789012
  Title: Machine Learning
  Author: Author C
  Publisher: Publisher Z
  Volume: 1
  Year: 2023
  Isbn: 3456789012

'''
