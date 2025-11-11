"""
Задача №1
1.1 Написать программу, которая расшифрует строку.
Каждая символ - это две цифры. Отчет с 00 -> 'a', 01 -> 'b' и до 25 -> 'z',
26 - это пробел, он не входит в набор букв
Вход: строка из цифр. Выход: Текст.

1.2 Реализовать и расшифровку и зашифровку через функции
In/Out: '070411111426152419071413' <-> Out/In: 'hello python'

1.3 Добавить обработку неправильных входных данных.

1.4 Написать тесты для отработки корректных и некорректных данных.

"""

import string
from unittest import case

SYMBOL_TABLE = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z",
    26: " ",
}


def get_char_to_digit_table() -> dict:
    return {value: key for key, value in SYMBOL_TABLE.items()}


def decode(text: str) -> str:
    """Расшифрование строки вида '000102030405' в 'abcdef'"""
    if not text:
        return ""
    if not text.isdigit():
        raise ValueError("Строка может содержать только десятичные цифры")
    text_len = len(text)
    if text_len % 2:
        raise ValueError("В строке может быть только чётное число цифр")

    result = ""
    idx = 0
    for _ in range(text_len // 2):
        char = text[idx : idx + 2]
        char_int = int(char)
        if char_int not in SYMBOL_TABLE:
            raise ValueError(f"Недопустимый код {char!r} в строке")
        result += SYMBOL_TABLE[char_int]
        idx += 2

    return result


def encode(text: str) -> str:
    """Шифрование строки вида 'abcdef' в '000102030405'"""
    if not text:
        return ""
    for char in text:
        if char.isupper():
            raise ValueError("Строка не может содержать заглавные буквы")
        if not (char.isalpha() or char.isspace()):
            raise ValueError("Строка может содержать только английские буквы и пробелы")

    result = ""
    encode_table = get_char_to_digit_table()
    for char in text:
        result += str(encode_table[char]).rjust(2, "0")

    return result


def get_string() -> str:
    return input("Enter the string: ")


def main():
    while True:
        mode = input("Mode: 'D' - Decode, 'E' - Encode, 'Q' - Quit ::\t")
        match mode.upper():
            case "Q":
                break
            case "D":
                print("Decoded string:", decode(get_string()))
                break
            case "E":
                print("Encoded string:", encode(get_string()))
                break


if __name__ == "__main__":
    main()
