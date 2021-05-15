from django.db import models
from django_quill.fields import QuillField



class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = QuillField()
    blog_image = models.ImageField(upload_to='home/static/images')
    blog_date = models.DateField(auto_now=True)
