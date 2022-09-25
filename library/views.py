from django.shortcuts import render
from .models import Book
from datetime import date


def list_books(request):
    my_dict = {
        'title': 'Библиотека',
        'books': Book.objects.all()

    }
    return render(request, 'library/list_books.html', my_dict)


def list_books_for_date(request, year, month, day):

    day = date(year, month, day)
    date_set = set()
    for i in Book.objects.all():
        date_set.add(i.date_pub)
    list_date = sorted(list(date_set))
    index_next_date = None
    index_previous_date = None

    if list_date.index(day) != 0:
        index_previous_date = list_date.index(day) - 1
    if list_date.index(day) != len(list_date) - 1:
        index_next_date = list_date.index(day) + 1
    previous_date = None
    if index_previous_date is not None:
        previous_date = list_date[index_previous_date]
    next_date = None
    if index_next_date is not None:
        next_date = list_date[index_next_date]

    my_dict = {
            'books': Book.objects.filter(date_pub=day),
            'title': f'Книги с датой {day}',
            'next_date': next_date,
            'prev_date': previous_date

        }

    return render(request, 'library/list_books_for_date.html', my_dict)
