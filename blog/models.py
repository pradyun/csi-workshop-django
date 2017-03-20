from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey('blog.Category')

    def get_short_body(self):
        return self.body[:150]+"...."

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title