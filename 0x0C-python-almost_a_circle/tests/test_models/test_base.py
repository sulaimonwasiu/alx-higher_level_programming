import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id(self):
        # Test if the id attribute is correctly assigned
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    
    def test_nb_objects(self):
        # Test if the __nb_objects attribute is incremented correctly
        b1 = Base()
        self.assertEqual(Base.get_nb_objects(), 3)

        b2 = Base()
        self.assertEqual(Base.get_nb_objects(), 4)

        b3 = Base(10)
        self.assertEqual(Base.get_nb_objects(), 4)
    

if __name__ == '__main__':
    unittest.main()
