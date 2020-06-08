from django.contrib import admin

# Register your models here.
from QueryTest.models import Topping, Pizza, Publication, Article


class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Topping, ToppingAdmin)


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_toppings']


admin.site.register(Pizza, PizzaAdmin)


# class PublicationAdmin(admin.ModelAdmin):
#     list_display = ['title']
#
#
# admin.site.register(Publication, PublicationAdmin)
#
#
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['headline', 'publications']
#
#
# admin.site.register(Article, ArticleAdmin)
