import unittest

from day2.encode_decode import encode, decode


class TestDecode(unittest.TestCase):
    def test_not_digit(self):
        """Проверка на не цифру"""
        self.assertRaises(ValueError, decode, "Aa")

    def test_not_even_number_of_symbols(self):
        """Проверка на нечётное количество цифр"""
        self.assertRaises(ValueError, decode, "010")

    def test_invalid_code(self):
        """Проверка на недопустимый код символа в строке"""
        self.assertRaises(ValueError, decode, "27")

    def test_ok(self):
        """Проверка на корректные данные"""
        self.assertEqual(decode("070411111426152419071413"), "hello python")


class TestEncode(unittest.TestCase):
    def test_not_lowercase(self):
        """Проверка на заглавную букву"""
        self.assertRaises(ValueError, encode, "A")

    def test_not_en_char_or_space(self):
        """Проверка на неанглийскую букву или пробел"""
        self.assertRaises(ValueError, encode, "-")

    def test_ok(self):
        """Проверка на корректные данные"""
        self.assertEqual(encode("hello python"), "070411111426152419071413")


if __name__ == "__main__":
    unittest.main()
