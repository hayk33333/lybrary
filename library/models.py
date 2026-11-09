from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.PositiveIntegerField()
    copies_available = models.PositiveIntegerField(default=0)

    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name='books'
    )

    genres = models.ManyToManyField(
        Genre,
        related_name='books'
    )

    def __str__(self):
        return self.title

    def is_available(self):
        return self.copies_available > 0


class Reader(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class Loan(models.Model):
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    returned_at = models.DateTimeField(null=True, blank=True)

    reader = models.ForeignKey(
        Reader,
        on_delete=models.PROTECT,
        related_name='loans'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='loans'
    )

    def __str__(self):
        return f"{self.reader} - {self.book}"

    def is_returned(self):
        return self.returned_at is not None

    def is_overdue(self):
        return (
            self.returned_at is None
            and self.due_date < timezone.localdate()
        )