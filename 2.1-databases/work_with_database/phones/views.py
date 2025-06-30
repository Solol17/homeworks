from django.shortcuts import render, redirect
from llm.cli import models

from phones.models import Phone

context = {}

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_param = request.GET.get('sort', 'name')  # по умолчанию сортируем по имени
    phone_objects = Phone.objects.all()

    if sort_param == 'name':
        phone_objects = phone_objects.order_by('name')
    elif sort_param == 'min_price':
        phone_objects = phone_objects.order_by('price')  # От дешевых к дорогим
    elif sort_param == 'max_price':
        phone_objects = phone_objects.order_by('-price')

    template = 'catalog.html'
    context['phones'] = phone_objects
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.get(slug=slug)
    template = 'product.html'
    context['phone'] = phone_object
    return render(request, template, context)
