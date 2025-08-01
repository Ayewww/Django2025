from django.contrib import admin
from .models import Post
from .models import Category

#blog/admin.py
admin.site.register(Post)
admin.site.register(Category)


