from django.contrib import admin
from .models import Post , captions , author , comments
# Register your models here.
admin.site.register(Post)
admin.site.register(captions)
admin.site.register(author)
admin.site.register(comments)