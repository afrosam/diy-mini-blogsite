from django.db import models
#from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from datetime import date
from django.utils import timezone
import uuid # Required for unique book instances

# Create your models here.
class Blogpage(models.Model):
    """Model representing a blog (but not a specific copy of a blog)."""
    title = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Blogger', null=True, on_delete=models.SET_NULL)

    description = models.TextField(max_length=1000, help_text='Enter the description of this blog.')

    class Meta:
        ordering = ['date', 'title']

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blogs/', args=[str(self.id)])

class Blogger(models.Model):
    """Model representing the author of the blog"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('bloggers/', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name}, {self.last_name}'

class Comment(models.Model):
    """Model representing the comments for each Blogpage"""
    description = models.TextField(max_length=1000, help_text='Enter your comment for this blog.', null=False)
    blog = models.ForeignKey('Blogpage', null=True, on_delete=models.SET_NULL)
    date = models.DateField(default=timezone.now, null=False)
    author = models.CharField(max_length=100)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('blog/', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.blog}'
