import unittest
from simple_calculator import SimpleCalculator 

class Test(unittest.TestCase):

    def setUp(self):
        self.calc= SimpleCalculator()    
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3),5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3),-1)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3),6)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2),2)
        

        