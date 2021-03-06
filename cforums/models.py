from django.db import models

class Image(models.Model):
    filename = models.CharField(max_length=100)
    file = models.ImageField(upload_to="static/uploads/%Y/%m/%d/")

class Post(models.Model):
    pid = models.PositiveIntegerField()
    pinned = models.BooleanField()
    reply_to = models.IntegerField()
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    creation_date = models.DateTimeField()
    images = models.ManyToManyField(Image, blank=True)
