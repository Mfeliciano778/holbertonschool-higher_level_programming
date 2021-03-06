#!/user/bin/python3
'''unittesting against base - python -m discover tests'''
import unittest
from models.base import Base


class Testbaseclass(unittest.TestCase):
    '''Testbaseclass - testing base'''

    def test_base(self):
        '''test_base - function to test base'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

if __name__ == '__main__':
    unittest.main()