from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Asset(models.Model):

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40)
    info = models.CharField(max_length=100)
    details = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='assets/')
    seen_by = models.ManyToManyField(User, related_name='seen_by', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Room(models.Model):
    asset = models.ManyToManyField(Asset, related_name='asset')
    participants = models.ManyToManyField(User, related_name='participants')


class Message(models.Model):

    room = models.ForeignKey(Room, related_name='room', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str_(self):
        return self.content