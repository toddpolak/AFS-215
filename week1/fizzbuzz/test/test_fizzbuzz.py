import pytest
from lib.fizzbuzz import fizzBuzz

def test1_fizzBuzz():
    test = fizzBuzz(1)
    assert test == '1'
    
def test2_fizzBuzz():
    test = fizzBuzz(2)
    assert test == '2'
    
def test3_fizzBuzz():
    test = fizzBuzz(3)
    assert test == '3'