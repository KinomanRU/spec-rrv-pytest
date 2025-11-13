import pytest
from django.urls import reverse
from books.models import Book


@pytest.fixture
def book(db):
    return Book.objects.create(
        title="Test Book",
        author="Test Author",
        description="Test Description",
        slug="test-book",
    )


@pytest.fixture
def book_list_response(client):
    url = reverse("books:book_list")
    return client.get(url)


@pytest.fixture
def book_detail_response(book, client):
    url = reverse("books:book_detail", kwargs={"slug": book.slug})
    return client.get(url)
