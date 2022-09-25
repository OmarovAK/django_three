from django.urls import path
from .views import list_books, list_books_for_date

app_name = 'library'

urlpatterns = [
    path('', list_books, name='list_books'),
    path('<int:year>-<int:month>-<int:day>', list_books_for_date, name='list_books_for_date'),



]
