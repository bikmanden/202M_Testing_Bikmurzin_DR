import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestTriangleType(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(2, 2, 2), "equilateral")
        self.assertEqual(get_triangle_type(10, 10, 10), "equilateral")

    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(9, 8, 7), "nonequilateral")

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 6), "isosceles")
        self.assertEqual(get_triangle_type(4, 2, 4), "isosceles")
        self.assertEqual(get_triangle_type(9, 9, 7), "isosceles")

    def test_incorrect_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, -1, -1)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, -1, 1)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-2, 2, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 2, -4)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 1, -1)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-2, -2, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, -2, -4)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-4, -4, -7)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 2)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2, 2, 0)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(5, 10, 16)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 0, 0)

if __name__ == '__main__':
    unittest.main()