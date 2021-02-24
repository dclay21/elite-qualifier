from main import check_name
import unittest
class TestCheckName(unittest.TestCase):

    def test_profanity(self):
      self.assertFalse(check_name("$hit"))
      self.assertTrue(check_name("John"))

    

    def test_alphaOnly(self):
      self.assertFalse(check_name("H4ppy"))
      self.assertTrue(check_name("Jackie"))


if __name__ == '__main__':
  unittest.main()