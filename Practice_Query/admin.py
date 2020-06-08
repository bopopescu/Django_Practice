from django.contrib import admin

# Register your models here.
from Practice_Query.models import Publisher, Book, Store, Details


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Publisher, PublisherAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'publisher']


admin.site.register(Book, BookAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_books']


admin.site.register(Store, StoreAdmin)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'publisher', 'get_books']


admin.site.register(Details, DetailsAdmin)
