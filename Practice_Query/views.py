from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from Practice_Query.models import Book, Publisher, Store, Details


def Pub(request):
    context = {
        'publisher': list(Publisher.objects.values()),
    }
    return JsonResponse(context, safe=False)


def Div(request):
    queryset = Book.objects.select_related('publisher').all()

    books = []

    for book in queryset:
        books.append({'name': book.name, 'publisher': book.publisher.name})
    context = {
        # 'publisher': list(Book.objects.values('id','name','price','publisher__name')),
        'publisher': list(books)
    }
    return JsonResponse(context, safe=False)


def Sto(request):
    # queryset = Store.objects.all()
    queryset = Store.objects.prefetch_related('books')
    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})
    context = {
        'publisher': list(stores),
    }
    return JsonResponse(context, safe=False)


def Det(request):
    # queryset = Store.objects.all()
    queryset = Details.objects.select_related('publisher').prefetch_related('books')
    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({'id': store.id, 'name': store.name, 'publisher': store.publisher.name, 'books': books})
    context = {
        'details': list(stores),
    }
    return JsonResponse(context, safe=False)
