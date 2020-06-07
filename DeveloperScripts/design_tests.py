'''
import unittest
    import one

    class TestOne(unittest.TestCase):
        def test_myfunc_one(self):
            y = 'a'
            result = one.myfunc(y)
            self.assertEqual(result, 'A')
        
        def test_myfunc_two(self):
            y = 'm'
            result = one.myfunc(y)
            self.assertEqual(result, 'M')

'''

from UI import designs
import unittest

class Designs:

    def dev_band(self):
        title = 'GAMES'
        designs.create_band(title)

if __name__ == '__main__':
    dsgn = Designs()
    dsgn.dev_band()