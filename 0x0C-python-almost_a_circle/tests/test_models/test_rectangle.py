#!/usr/bin/python3
"""Test Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""
    def test_1_id(self):
        """Test if the id attribute is correctly assigned"""
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
        """Test if the width attribute is correctly assigned"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.width, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)

    def test_3_area(self):
        """Test area method"""
        r4 = Rectangle(3, 2)
        self.assertEqual(r4.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_4_update(self):
        """Test update method"""
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

    def test_5_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary,
                         {'x': 1, 'y': 9, 'id': 11, 'height': 2, 'width': 10})

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r2_dictionary, r1_dictionary)


if __name__ == '__main__':
    unittest.main()
