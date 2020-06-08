from django.urls import path

# custom app
from .views import *


urlpatterns = [

    # sign-up api
    path('sign-up/', Registration),
    # path('employer/login/', login),
    # path('employer/logout/', logout),
]