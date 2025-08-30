import io
import sys
import pytest
from book import Book  # Ensure this is importing from the correct file

class TestBook:
    '''Tests for the Book class'''

    def test_has_title_and_page_count(self):
        '''Test that the book has a title and page count passed into the __init__ method.'''
        book = Book("And Then There Were None", 272)
        assert book.page_count == 272
        assert book.title == "And Then There Were None"

    def test_requires_int_page_count(self):
        '''Test that setting page_count to a non-integer value prints the error message.'''
        book = Book("And Then There Were None", 272)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"  # This should trigger the error
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "page_count must be an integer\n"

    def test_can_turn_page(self):
        '''Test the turn_page method outputs the correct message.'''
        book = Book("The World According to Garp", 69)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()  # Assuming this method exists and works
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Flipping the page...wow, you read fast!\n"
