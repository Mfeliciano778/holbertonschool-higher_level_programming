#!/user/bin/python3
'''unittesting against base - python -m discover tests'''
import unittest
from models.rectangle import Rectangle


class Testrectclass(unittest.TestCase):
    '''Testrectclass - testing rect'''

    def test_rectangle(self):
        '''test_rect - function to test rect'''
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

if __name__ == '__main__':
    unittest.main()