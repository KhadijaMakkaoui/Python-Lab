import unittest
from simple_calculator import SimpleCalculator 

class Test(unittest.TestCase):

    def setUp(self):
        self.calculator= SimpleCalculator()    
    
    def test_add(self):
        result= self.calculator.add(2, 3)
        self.assertEqual(result,5)

    def test_add(self):
        result= self.calculator.subtract(2, 3)
        self.assertEqual(result,-1)
    
    def test_multiply(self):
        result= self.calculator.multiply(2, 3)
        self.assertEqual(result,6)
    
    def test_divide(self):
        result= self.calculator.divide(4, 2)
        self.assertEqual(result,2)
        

        