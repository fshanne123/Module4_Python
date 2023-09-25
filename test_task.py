import unittest

def check(x):
        return x >= 100

class TestTask(unittest.TestCase):

    def test(self):
        self.assertTrue(check(123), True)

if __name__ == '__main___':

    unittest.main()
