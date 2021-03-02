from django.db import models

class Image(models.Model):
    filename = models.CharField(max_length=100)
    file = models.ImageField(upload_to="static/uploads/%Y/%m/%d/")


class Post(models.Model):
    pid = models.PositiveIntegerField()
    pinned = models.BooleanField()
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    creation_date = models.DateTimeField()
    images = models.ManyToManyField(Image)


class Reply(models.Model):
    rid = models.PositiveIntegerField()
    pinned = models.BooleanField()
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    reply_to = models.PositiveIntegerField()
    creation_date = models.DateTimeField()
    images = models.ManyToManyField(Image)
