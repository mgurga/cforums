
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.conf import settings
from django.db import OperationalError

from cforums.models import Post
from cforums.models import Image

class TopicView(View):
    def get(self, request, topic):
        posts = []

        try:
            for p in Post.objects.filter(topic=topic, reply_to=0):
                post = {
                    "title": p.title,
                    "creation_date": p.creation_date,
                    "id": p.pid,
                }

                posts.append(post)
        except OperationalError:
            pass

        return render(request, "topic.html", {"topic": topic, "posts": posts})
