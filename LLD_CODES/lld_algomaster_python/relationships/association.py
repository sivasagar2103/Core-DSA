'''

'''

#Unidirectional
class Driver:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, driver):
        self.driver = driver
    
    def drive(self):
        print(f'{self.driver.name} driving the car')


#Bidirectional
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    

class Book:
    def __init__(self, title):
        self.title = title
        self.author = None
    
    def set_author(self, author):
        self.author = author
