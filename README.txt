# Library Management System

## Նկարագրություն

Գրադարանի կառավարման համակարգ՝ ստեղծված Django
Framework-ի և MySQL տվյալների բազայի միջոցով։

## Տեխնոլոգիաներ

- Python
- Django
- MySQL
- Django ORM

## Models

- Author
- Genre
- Book
- Reader
- Loan

## Database Relationships

- Author → Book (One-to-Many)
- Book ↔ Genre (Many-to-Many)
- Reader → Loan (One-to-Many)
- Book → Loan (One-to-Many)

## Տեղադրում

1. Ստեղծել virtual environment։

python -m venv venv

2. Ակտիվացնել այն։

venv\Scripts\activate

3. Տեղադրել գրադարանները։

pip install django mysqlclient

4. Կատարել migrations։

python manage.py makemigrations
python manage.py migrate

5. Ստեղծել superuser։

python manage.py createsuperuser

6. Գործարկել նախագիծը։

python manage.py runserver