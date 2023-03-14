from unittest import TestCase
import ai
from dotenv import load_dotenv


class Test(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        load_dotenv()

    def test_get_code(self):
        result = ai.get_code("convert csv to json")
        print(result)
