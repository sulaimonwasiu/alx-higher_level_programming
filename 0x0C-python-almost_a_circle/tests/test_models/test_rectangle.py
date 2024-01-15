#!/usr/bin/python3

"""Unittest for Rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_1_id(self):
        # Test if the id attribute is correctly assigned
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


        self.assertRaises(ValueError, Rectangle, 0, 0)

        r5 = Rectangle(1, 1)
        self.assertEqual(r5.id, 4)

        r6 = Rectangle(1000000, 1000000)
        self.assertEqual(r6.id, 5)

    def test_2_width(self):
        # Test if the width attribute is correctly assigned
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
    
    
    def test_3_area(self):
        # Test if the area method returns the correct area
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

        
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)
    
        
    def test_4_update(self):
        # Test if the update method correctly assigns attributes
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

        self.assertRaises(IndexError, r1.update, 89, 2, 3, 4, 5, 6)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
    

if __name__ == '__main__':
    unittest.main()