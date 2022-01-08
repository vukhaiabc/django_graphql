from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    createAt = models.DateTimeField(auto_now_add=True)
    des = models.TextField(default='')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author,related_name='books')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')
    headline = models.CharField(max_length=255)
    pub_date = models.DateField()
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.name


