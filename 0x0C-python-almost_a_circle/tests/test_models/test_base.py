import unittest
from unittest.mock import patch
from io import StringIO
import json
import csv
import turtle
from models.base import Base
# Replace 'your_module' with the actual module name
from models.rectangle import Rectangle
class TestBase(unittest.TestCase):

    def setUp(self):
        self.base_instance = Base()

    def tearDown(self):
        del self.base_instance

    def test_to_json_string(self):
        # Test when list_dictionaries is empty
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test when list_dictionaries has values
        list_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        expected_json = json.dumps(list_dicts)
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_from_json_string(self):
        # Test when json_string is empty
        self.assertEqual(Base.from_json_string(""), [])

        # Test when json_string has values
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        expected_list = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        self.assertEqual(Base.from_json_string(json_string), expected_list)

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='[{"id": 1}]') # type: ignore
    def test_load_from_file(self, mock_open):
        # Test when the file exists
        expected_list = [Base(1)]
        self.assertEqual(Base.load_from_file(), expected_list)

        # Test when the file does not exist
        mock_open.side_effect = IOError
        self.assertEqual(Base.load_from_file(), [])

    @patch('builtins.open', new_callable=unittest.mock.mock_open) # type: ignore
    def test_save_to_file(self, mock_open):
        # Test when list_objs is None
        Base.save_to_file(None)
        mock_open.assert_called_with('Base.json', 'w')
        handle = mock_open()
        handle.write.assert_called_with('[]')

        # Test when list_objs is not None
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])
        mock_open.assert_called_with('Base.json', 'w')
        handle = mock_open()
        expected_data = '[{"id": 1}, {"id": 2}]'
        handle.write.assert_called_with(expected_data)

    # Add more test methods for other class methods

if __name__ == '__main__':
    unittest.main()
