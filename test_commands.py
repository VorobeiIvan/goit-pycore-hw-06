import unittest
from src.commands import add_contact, change_contact, show_phone, show_all

class TestCommands(unittest.TestCase):
    def setUp(self):
        self.contacts = {}

    def test_add_contact(self):
        result = add_contact(["John", "1234567890"], self.contacts)
        self.assertEqual(result, "Contact added.")
        self.assertIn("John", self.contacts)

    def test_change_contact(self):
        self.contacts["John"] = "1234567890"
        result = change_contact(["John", "0987654321"], self.contacts)
        self.assertEqual(result, "Contact updated.")
        self.assertEqual(self.contacts["John"], "0987654321")

    def test_show_phone(self):
        self.contacts["John"] = "1234567890"
        result = show_phone(["John"], self.contacts)
        self.assertEqual(result, "1234567890")

    def test_show_all(self):
        self.contacts["John"] = "1234567890"
        result = show_all(self.contacts)
        self.assertIn("John: 1234567890", result)

if __name__ == "__main__":
    unittest.main()
