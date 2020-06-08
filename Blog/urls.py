from django.urls import path

# custom app
from .views import *


urlpatterns = [

    # sign-up api
    path('create/', create),
    # path('employer/login/', login),
    # path('employer/logout/', logout),
]