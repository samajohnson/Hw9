import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        person1 = BookLover("Max Francisco", "maxfrancisco6@gmail.com", "mystery")
        book = "THE LIFE OF PI"
        person1.add_book("THE LIFE OF PI", 4)  
        message = "Test value is not true."
        result = (person1.book_list['book_name'] == book).any()
        self.assertTrue(result, message)
        
        
    def test_2_add_book(self):
        person1 = BookLover("Max Francisco", "maxfrancisco6@gmail.com", "mystery")
        book = "THE LIFE OF PI"
        person1.add_book("THE LIFE OF PI", 4)  
        person1.add_book("THE LIFE OF PI", 5) 
        numbooks = len(person1.book_list)
        message = "Test value is not true."
        self.assertTrue(numbooks == 1, message)
        

    def test_3_has_read(self):
        person1 = BookLover("Max Francisco", "maxfrancisco6@gmail.com", "mystery")
        book = "THE LIFE OF PI"
        person1.add_book("THE LIFE OF PI", 4)  
        message = "Test value is not true."
        result = person1.had_read("THE LIFE OF PI") 
        self.assertTrue(result, message)        
        
    def test_4_has_read(self):
        person1 = BookLover("Max Francisco", "maxfrancisco6@gmail.com", "mystery")
        book = "THE LIFE OF PI"
        person1.add_book("THE LIFE OF PI", 4) 
        message = "Test value is not true."
        result = person1.had_read("the crucible") 
        self.assertFalse(result, message)         
        
        
        
    def test_5_num_books_read(self):
        person1 = BookLover("Max Francisco", "maxfrancisco6@gmail.com", "mystery")
        person1.add_book("THE LIFE OF PI", 4)  
        person1.add_book("the crucible", 1)
        person1.add_book("The Help", 4)
        expected = 3
        message = "Test value is not true."
        person1.num_books_read()
        self.assertEqual(person1.num_books, expected)
        
    def test_6_fav_books(self):
        person1 = BookLover("Max Francisco", "maxfrancisco6@gmail.com", "mystery")
        person1.add_book("THE LIFE OF PI", 4)  
        person1.add_book("the crucible", 1)
        person1.add_book("The Help", 4)
        person1.fav_books()
        message = "Test value is not true."
        result = (person1.filtered_list['book_rating'] > 3).all()
        self.assertTrue(result, message)
    
    
    
if __name__ == '__main__':
    unittest.main(verbosity=3)
