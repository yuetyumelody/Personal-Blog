from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateField()
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )

    body = models.TextField()

    def __str__(self):
        return self.title

class RecipePost(models.Model):
    title = models.CharField(max_length=200)
    date_posted = models.DateField()
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )

    body = models.TextField()

    def __str__(self):
        return self.title
