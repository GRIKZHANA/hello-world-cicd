import unittest
from app import hello_world, welcome_message


class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(
            hello_world(),
            "Hello, DevOps!"
        )

    def test_hello_world_return_type(self):
        self.assertIsInstance(hello_world(), str)

    def test_welcome_message_first_name(self):
        self.assertEqual(
            welcome_message("Alice"),
            "Welcome to DevOps, Alice!"
        )

    def test_welcome_message_second_name(self):
        self.assertEqual(
            welcome_message("Bob"),
            "Welcome to DevOps, Bob!"
        )


if __name__ == "__main__":
    unittest.main()
