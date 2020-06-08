from django.contrib import admin

# Register your models here.
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']


admin.site.register(Post, PostAdmin)
