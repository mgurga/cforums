from django.db import models

class Image(models.Model):
    filename = models.CharField(max_length=100)
    file = models.ImageField(upload_to="uploads/%Y/%m/%d/")

class Post(models.Model):
    pinned = models.BooleanField()
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    id = models.BigAutoField()
    creation_date = models.DateTimeField()
    images = models.ManyToManyField(Image)

class Reply(models.Model):
    topic = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body = models.TextField()
    reply_to = models.BigAutoField()
    id = models.BigAutoField()
    creation_date = models.DateTimeField()
    images = models.ManyToManyField(Image)
