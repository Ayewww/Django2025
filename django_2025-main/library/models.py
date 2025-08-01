from django.db import models

#blog/models.py
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,
                                        null=True)
    updated_date = models.DateTimeField(auto_now=True,
                                        null=True)
    uploaded_image = models.ImageField(upload_to='images/',
                                       blank=True,)
    uploaded_file = models.FileField(upload_to='files/',
                                       blank=True,)

    def __str__(self):
        return f'게시글제목: {self.title} - 게시글내용 - {self.content} - 생성시간 - {self.created_date} - 업데이트-{self.updated_date}'
    def get_absolute_url(self):
        return f'/library/{self.pk}/'