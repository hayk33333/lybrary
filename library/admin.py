from django.contrib import admin
from .models import Author, Genre, Book, Reader, Loan

# Register your models here.
class LoanInline(admin.TabularInline):
    model = Loan
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_year')
    search_fields = ('first_name', 'last_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'copies_available')
    search_fields = ('title',)
    list_filter = ('author', 'genres')


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name', 'email')
    inlines = [LoanInline]


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'reader',
        'book',
        'borrowed_at',
        'due_date',
        'returned_at'
    )
    list_filter = ('returned_at',)
    search_fields = ('reader__full_name', 'book__title')