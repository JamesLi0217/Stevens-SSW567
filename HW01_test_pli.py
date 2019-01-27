'''
@Title: Testing triangle classification
@Author: PuzhuoLi  CWID:10439435
@Date: 2019-01-26 13:24:16
'''


import unittest
import math
from HW01_pli import *



class TestTriangle(unittest.TestCase):
    '''
        Test HW01 triangle classification
        equilateral triangles have all three sides with the same length
        isosceles triangles have two sides with the same length
        scalene triangles have three sides with different lengths
        right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
    '''
    # test 8 case 
    def test_classify_triangle1(self):
        self.assertEqual("It is a isoscele triangle and a right triangle as well!", classify_triangle(1, 1, math.sqrt(2)))
    def test_classify_triangle2(self):    
        self.assertEqual("It is a right triangle!", classify_triangle(5, 4, 3))
    def test_classify_triangle3(self):
        self.assertEqual("It is an equilateral triangle but not a right triangle!", classify_triangle(3, 3, 3))
    def test_classify_triangle4(self):
        self.assertEqual("It is a isoscele triangle but not a right triangle!", classify_triangle(3, 3, 4))
    def test_classify_triangle5(self):
        self.assertEqual("It is a scalene triangle and not a right triangle!", classify_triangle(2, 3, 4))
    def test_classify_triangle6(self):
        self.assertEqual("Please double check the enter, it is not a triangle", classify_triangle(1, 2, 3))
    def test_classify_triangle7(self): 
        with self.assertRaises(TypeError):
            classify_triangle(1, 2, "l")
    def test_classify_triangle8(self): 
        with self.assertRaises(ValueError):
            classify_triangle(1, 2, -13)


if __name__ == "__main__":
    unittest.main()

