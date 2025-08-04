from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    slug = models.SlugField(max_length=1100, unique=True, allow_unicode=True, null=True)
    def get_url(self):
        return f'/blog/category/{self.slug}'
    def __str__(self):
        return f'{self.name}----{self.slug}'

#blog/models.py
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,
                                        null=True)
    updated_date = models.DateTimeField(auto_now=True,
                                        null=True)
    uploaded_image = models.ImageField(upload_to='images/',
                                       blank=True,)
    uploaded_file = models.FileField(upload_to='files/',
                                       blank=True,)
    

    def __str__(self):
        return f'게시글제목: {self.title} - 게시글내용 - {self.content} - 작성자 - {self.author} - 카테고리-{self.category}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,
                                        null=True)
    updated_date = models.DateTimeField(auto_now=True,
                                        null=True)
    
    def __str__(self):
        return (f'{self.author.username}--{self.content} in {self.post.title}')