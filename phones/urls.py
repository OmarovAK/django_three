from django.urls import path
from .views import list_phones, phones_detail


app_name = 'phones'
urlpatterns = [
    path('', list_phones, name='list_phones'),
    path('phone_detail/<slug:slug>', phones_detail, name='phones_detail'),

]
