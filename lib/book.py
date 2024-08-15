class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Use a private attribute for validation
        self.page_count = page_count  # Use the property setter for validation

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def __repr__(self):
        return f"Book(title='{self.title}', page_count={self._page_count})"

# Example of usage
if __name__ == "__main__":
    book = Book("And Then There Were None", 272)
    print(book)  # Should print: Book(title='And Then There Were None', page_count=272)
    book.turn_page()  # Should print: Flipping the page...wow, you read fast!
