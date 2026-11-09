from .models import Author, Genre, Book, Reader, Loan


def get_author_books(author):
    return author.books.all()


def get_genre_books(genre):
    return genre.books.all()


def get_book_genres(book):
    return book.genres.all()


def get_reader_loans(reader):
    return reader.loans.all()


def get_active_loans():
    return Loan.objects.filter(returned_at__isnull=True)


def print_reader_books(reader):
    loans = reader.loans.select_related(
        'book',
        'book__author'
    )

    for loan in loans:
        print(
            f"{loan.book.title} — "
            f"{loan.book.author.full_name()} — "
            f"{loan.due_date}"
        )