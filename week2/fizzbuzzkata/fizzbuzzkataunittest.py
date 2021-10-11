import unittest
from fizzbuzzkata import FizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def test1_fizzBuzz(self):
        test = FizzBuzz(1)
        assert test == '1'
        
    def test2_fizzBuzz(self):
        test = FizzBuzz(2)
        assert test == '2'
        
    def test3_fizzBuzz(self):
        test = FizzBuzz(3)
        assert test == 'Fizz'
        
    def test4_fizzBuzz(self):
        test = FizzBuzz(5)
        assert test == 'Buzz'
        
    def test5_fizzBuzz(self):
        test = FizzBuzz(6)
        assert test == 'Fizz'
        
    def test6_fizzBuzz(self):
        test = FizzBuzz(10)
        assert test == 'Buzz'
        
    def test7_fizzBuzz(self):
        test = FizzBuzz(15)
        assert test == 'FizzBuzz'

if __name__ == '__main__':
    unittest.main()