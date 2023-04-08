import unittest
from io import StringIO
from unittest.mock import patch
from say_my_name import say_my_name


class TestHandlerCase(unittest.TestCase):

    def test(self):
        name = 'testmycode'
        expected_output = '{}??? You are right !!!\n'.format(name)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            say_my_name(name)
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()          