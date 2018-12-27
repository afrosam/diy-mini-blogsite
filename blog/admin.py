from django.contrib import admin

# Register your models here.
from blog.models import Blogpage, Blogger

admin.site.register(Blogpage)
admin.site.register(Blogger)
