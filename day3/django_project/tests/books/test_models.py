from django.urls import reverse


def test_book_content(book):
    assert book.title == "Test Book"
    assert book.author == "Test Author"
    assert book.description == "Test Description"


def test_book_slug(book):
    assert book.slug == "test-book"
    assert book.slug != "test-book-2"


def test_book_methods(book):
    assert str(book) == "Test Book"
    assert book.get_absolute_url() == reverse(
        "books:book_detail", kwargs={"slug": book.slug}
    )
