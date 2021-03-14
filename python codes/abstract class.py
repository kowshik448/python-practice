from abc import ABCMeta, abstractmethod
class Book():
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod

    def display(self):
        pass

class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price=price
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"price: {self.price}")

title= input()
author= input()
price= int(input())
new_book=MyBook(title,author,price)
new_book.display()
    