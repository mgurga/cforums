
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.conf import settings

from cforums.models import Post
from cforums.models import Reply
from cforums.models import Image

class TopicView(View):
    def get(self, request, topic):
        posts = []

        for p in Post.objects.filter(topic=topic):
            post = {
                "title": p.title,
                "creation_date": p.creation_date,
                "id": p.pid,
            }

            posts.append(post)

        return render(request, "topic.html", {"topic": topic, "posts": posts})
