from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    description = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title