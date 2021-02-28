
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings

def home_view(request):
    return render(request, "home.html", {"topics": settings.TOPICS, "forumtitle": settings.TITLE})

def topic_view(request, topic):
    return render(request, "topic.html", {"topic": topic})