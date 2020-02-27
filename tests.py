import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_pi(self):
        expected = 28
        self.assertEqual(expected, task.pi())

    def test_list(self):
        first = "apple"
        last = "cherry"
        self.assertEqual((first, last), task.list())

    def test_time(self):
        expected = 365
        self.assertEqual(expected, task.time())


if __name__ == '__main__':
    unittest.main()
