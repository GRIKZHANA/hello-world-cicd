import unittest
from app import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_hello_world_message(self):
        self.assertEqual(
            hello_world(),
            "Hello, DevOps!"
        )

    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_world(), str)


if __name__ == "__main__":
    unittest.main()
