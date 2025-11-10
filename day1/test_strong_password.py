import unittest
import day1.strong_password as strong_password


class TestCheckPassword(unittest.TestCase):
    def test_length(self):
        self.assertFalse(strong_password.check_password("Aa1_111")[0])
        self.assertFalse(strong_password.check_password("Aa1_1111111111111111111")[0])
        self.assertFalse(strong_password.check_password("")[0])

    def test_digit(self):
        self.assertFalse(strong_password.check_password("AaX_XXXX")[0])

    def test_lowercase(self):
        self.assertFalse(strong_password.check_password("AX1_11111")[0])

    def test_uppercase(self):
        self.assertFalse(strong_password.check_password("xa1_11111")[0])

    def test_special(self):
        self.assertFalse(strong_password.check_password("Aa1x11111")[0])

    def test_valid_password(self):
        self.assertTrue(strong_password.check_password("Aa1_11111")[0])


if __name__ == "__main__":
    unittest.main()
