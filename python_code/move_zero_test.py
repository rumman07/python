import unittest
import move_zero

class MoveZeroTest(unittest.TestCase):

    def test_one(self):
        list = [0,1,2,2,3,0,4,2]
        result = move_zero.move_zero(list)
        self.assertEqual(result, [1, 2, 2, 3, 4, 2, 0, 0])


if __name__ == '__main__':
    unittest.main()