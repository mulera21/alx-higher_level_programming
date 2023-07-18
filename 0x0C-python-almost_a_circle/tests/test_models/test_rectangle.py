import unittest
from models.rectangle import Rectangle
class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_width(self):
        self.assertEqual(self.rectangle.width, 5)
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"
        with self.assertRaises(ValueError):
            self.rectangle.width = -5

    def test_height(self):
        self.assertEqual(self.rectangle.height, 10)
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid"
        with self.assertRaises(ValueError):
            self.rectangle.height = -10

    def test_x(self):
        self.assertEqual(self.rectangle.x, 2)
        with self.assertRaises(ValueError):
            self.rectangle.x = -2

    def test_y(self):
        self.assertEqual(self.rectangle.y, 3)
        with self.assertRaises(ValueError):
            self.rectangle.y = -3

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 50)

    

    def test_update(self):
        self.rectangle.update(2, 8, 15, 4, 5)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 8)
        self.assertEqual(self.rectangle.height, 15)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)

        self.rectangle.update(height=20, x=6)
        self.assertEqual(self.rectangle.height, 20)
        self.assertEqual(self.rectangle.x, 6)

    def test_str(self):
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(self.rectangle), expected_output)

if __name__ == '__main__':
    unittest.main()
