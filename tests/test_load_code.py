from unittest import TestCase
from load_code import run_function


class Test(TestCase):
    def test_run_function(self):
        code_string = "def my_function(parameter):\n    return parameter.upper().split(' ')"

        result = run_function(code_string, "hello, world!")

        self.assertEqual(result, ['HELLO,', 'WORLD!'])
