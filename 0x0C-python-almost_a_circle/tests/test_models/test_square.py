import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size_property(self):
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update(self):
        square = Square(5)
        square.update(2, 10, 3, 4)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

        square.update(size=15, x=5)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 5)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        expected_dict = {"id": 1, "size": 5, "x": 2, "y": 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_str(self):
        square = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square), expected_output)


if __name__ == '__main__':
    unittest.main()
