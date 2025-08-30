import io
import sys
import pytest
from shoe import Shoe  # Ensure this is importing from the correct file

class TestShoe:
    '''Tests for the Shoe class'''

    def test_has_brand_and_size(self):
        '''Test that the shoe has a brand and size passed into the __init__ method.'''
        stan_smith = Shoe("Adidas", 9)
        assert stan_smith.brand == "Adidas"
        assert stan_smith.size == 9

    def test_requires_int_size(self):
        '''Test that setting size to a non-integer value prints the error message.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.size = "not an integer"  # This should trigger the error
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "size must be an integer\n"

    def test_can_cobble(self):
        '''Test that cobble method repairs the shoe and prints the correct message.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()  # Assuming this method exists and works
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Your shoe is as good as new!\n"

    def test_cobble_makes_new(self):
        '''Test that cobble method sets the condition to "New" after repair.'''
        stan_smith = Shoe("Adidas", 9)
        stan_smith.cobble()  # Assuming this method exists and works
        assert stan_smith.condition == "New"
