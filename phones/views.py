from django.shortcuts import render
from .models import Phones


def index(request):
    my_list = {
        'title': 'Главная страница',

    }
    return render(request, 'phones/index.html', my_list)

def list_phones(request):
    sort = request.GET.get('sort')
    if sort == 'min_price':
        phones_model = Phones.objects.order_by('price')
    elif sort == 'max_price':
        phones_model = Phones.objects.order_by('-price')
    elif sort == 'name':
        phones_model = Phones.objects.order_by('name')
    else:
        phones_model = Phones.objects.all()

    my_dict = {
        'title': 'Страница с телефонами',
        'phones': phones_model,
    }
    return render(request, 'phones/list_phones.html', my_dict)


def phones_detail(request, slug):
    phones_details = Phones.objects.get(slug=slug)
    my_dict = {
        'title': phones_details.name,
        'phone': phones_details
    }
    return render(request, 'phones/phone_detail.html', my_dict)
