# Assignment 1: Simple Book Class with Inheritance

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"'{self.title}' by {self.author}"


class FictionBook(Book):
    def __init__(self, title, author, genre):
        super().__init__(title, author)
        self.genre = genre

    def get_info(self):
        return f"{super().get_info()} - Fiction, {self.genre}"


class NonFictionBook(Book):
    def __init__(self, title, author, subject):
        super().__init__(title, author)
        self.subject = subject

    def get_info(self):
        return f"{super().get_info()} - Non-Fiction, {self.subject}"


# Demo
novel = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
biography = NonFictionBook("Steve Jobs", "i really dont know", "Biography")

print(novel.get_info())
print(biography.get_info())