from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book
from django.template.loader import render_to_string

from datetime import datetime

context = {}

def books_view(request):
    template = 'books/books_list.html'
    return render(request, template, context)

def list_book(request):
    books = Book.objects.all().order_by('pub_date')
    context['books'] = books
    template = 'books/books_list.html'
    return render(request, template, context)

def book_date(request, date=None):
    if date:
        try:
            date = datetime.strptime(date, '%Y-%m-%d').date()
            book_objects = Book.objects.filter(pub_date=date)
            previous_books = Book.objects.filter(pub_date__lt=date).order_by('-pub_date')
            next_books = Book.objects.filter(pub_date__gt=date).order_by('pub_date')
            if previous_books.exists():
                previous_date = previous_books.first().pub_date.strftime('%Y-%m-%d')
            else:
                previous_date = None

            if next_books.exists():
                next_date = next_books.first().pub_date.strftime('%Y-%m-%d')
            else:
                next_date = None

            context['previous_date']=previous_date
            context['next_date']=next_date
            context['books'] = book_objects
            page_number = int(request.GET.get('page', 1))

            books_list = [f'{book.name}, {book.author}, {book.pub_date}' for book in book_objects]
            paginator = Paginator(books_list, 1)
            page = paginator.get_page(page_number)
            context['page'] = page
            return render(request, 'books/book_date.html', context)

        except ValueError:
            return HttpResponse(f'Неверная дата')
    else:
        pass