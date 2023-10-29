import pandas as pd
import numpy as np

class BookLover():
    name = ""
    email = ""
    fav_genre = ""
    num_books = 0
    book_list = pd.DataFrame(columns = ['book_name', 'book_rating'])

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name': [], 'book_rating': []})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
   


    def add_book(self, book_name, rating):
        if (self.book_list['book_name'] == book_name).any():
            print("This book is already in the list.")
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
     
    def had_read(self, book_name):
        if  (self.book_list['book_name'] == book_name).any():
            return True
        else:
            return False
    
    
    def num_books_read(self):
        self.num_books = len(self.book_list)
        
    def fav_books(self):
        self.filtered_list = self.book_list[self.book_list['book_rating'] > 3]