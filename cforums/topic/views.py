
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.conf import settings

class TopicView(View):
    def get(self, request, topic):
        return render(request, "topic.html", {"topic": topic})
