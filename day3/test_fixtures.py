"""
### Упражнения для практики

1. Создайте тестовый файл с именем `test_fixtures.py`.

2. Напишите несколько фикстур — функций с декоратором `@pytest.fixture()` — которые возвращают данные (список, словарь или кортеж).

3. Для каждой фикстуры напишите хотя бы одну тестовую функцию, которая её использует.

4. Напишите два теста, использующих одну и ту же фикстуру.

5. Запустите `pytest --setup-show test_fixtures.py`. Все ли фикстуры запускаются перед каждым тестом?

6. Добавьте `scope='module'` к фикстуре из упражнения 4.

7. Повторно запустите `pytest --setup-show test_fixtures.py`. Что изменилось?

8. Для фикстуры из упражнения 6 измените `return <data>` на `yield <data>`.

9. Добавьте операторы `print` перед и после `yield`.

10. Запустите `pytest -s -v test_fixtures.py`. Имеет ли вывод смысл?

11. Выполните команду `pytest --fixtures`. Видите ли вы список своих фикстур?

12. Добавьте строку документации к одной из ваших фикстур, если вы её ещё не добавили. Повторно выполните команду `pytest --fixtures`, чтобы увидеть описание.
"""

from collections.abc import Generator

import pytest


@pytest.fixture(scope="module")
def get_list() -> Generator:
    """Return list"""
    print("\nget_list setup")
    yield [i for i in range(10)]
    print("\nget_list teardown")


@pytest.fixture(scope="module")
def get_tuple(get_list) -> Generator:
    """Return tuple"""
    print("\nget_tuple setup")
    yield tuple(get_list)
    print("\nget_tuple teardown")


@pytest.fixture(scope="module")
def get_dict(get_tuple) -> Generator:
    """Return dict"""
    print("\nget_dict setup")
    yield {i: str(i) for i in get_tuple}
    print("\nget_dict teardown")


class TestList:
    """Tests for list"""

    def test_type(self, get_list) -> None:
        """Test type"""
        assert type(get_list) is list

    def test_len(self, get_list) -> None:
        """Test len"""
        assert len(get_list) == 10


class TestTuple:
    """Tests for tuple"""

    def test_type(self, get_tuple) -> None:
        """Test type"""
        assert type(get_tuple) is tuple

    def test_len(self, get_tuple) -> None:
        """Test len"""
        assert len(get_tuple) == 10


class TestDict:
    """Tests for dict"""

    def test_type(self, get_dict) -> None:
        """Test type"""
        assert type(get_dict) is dict

    def test_len(self, get_dict) -> None:
        """Test len"""
        assert len(get_dict) == 10
