from django.contrib import admin
from .models import Post
from .models import Category
from .models import Comment
#blog/admin.py
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

