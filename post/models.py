from django.db import models
from django.utils.text import slugify
from datetime import date
# Create your models here.
class captions(models.Model):
    name_caption = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_caption

class author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name

class comments(models.Model):
    title = models.CharField(null=True , max_length= 150)
    comments = models.TextField(max_length=250)


class Post(models.Model):
    title = models.CharField(max_length=50)
    author_name = models.ForeignKey(author, on_delete=models.PROTECT , null=True)
    excerpt = models.CharField(max_length=50)
    image_name = models.ImageField(upload_to = "images")
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="",null=False)
    content = models.CharField(max_length=250)
    caption = models.ManyToManyField(captions)
    comments_line = models.ForeignKey(comments,on_delete=models.CASCADE,null=True)

    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
