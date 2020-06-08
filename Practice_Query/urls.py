from django.urls import path

from .views import *

urlpatterns = [

    path('books/', Pub),
    path('book/', Div),
    path('store/', Sto),
    path('details/', Det),

]
