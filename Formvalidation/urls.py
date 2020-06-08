from django.urls import path
from . import views
# custom app
from .views import *


urlpatterns = [

    # sign-up api
    path('signup/', Signup.as_view()),
    # path('employer/login/', login),
    # path('employer/logout/', logout),
]