from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=150)
    bio = models.TextField(max_length=300, blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    body_text = models.TextField()
    title = models.CharField(max_length=150)
    authors = models.ManyToManyField(Author, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    FEELINGS_CHOICE = [
        ('Love', 'Love'),
        ('Sad', 'Sad'),
        ('Happy', 'Happy'),
        ('Angry', 'Angry'),
        ('Funny', 'Funny'),
        ('Reflexive', 'Reflexive')
    ]
    feeling = models.CharField(
        max_length=50, choices=FEELINGS_CHOICE, default='sad')

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + ', ' + self.quote.title
