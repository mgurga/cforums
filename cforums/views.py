
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone

from .forms import PostForm

from .models import Post
from .models import Reply
from .models import Image

def home_view(request):
    return render(request, "home.html", {"topics": settings.TOPICS, "forumtitle": settings.TITLE})

def post_view(request, topic):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            postimage = Image.objects.create(
                file=request.FILES["image"],
                filename=request.FILES["image"].name
            )

            postimage.save()

            newpost = Post.objects.create(
                pid=get_id(topic),
                title=form.cleaned_data["title"],
                pinned=False,
                topic=topic,
                body=form.cleaned_data["body"],
                creation_date=timezone.localtime(),
            )

            newpost.images.add(postimage)

            newpost.save()

            return HttpResponseRedirect("/topic/" + topic)
    else:
        form = PostForm()

    return render(request, "post.html", {"form": form, "topic": topic})

def full_post(request, topic, id):
    post = Post.objects.filter(topic=topic).get(pid=id)
    images = post.images.all().first()
    return render(request, "fullpost.html", {"topic": topic, "post": post, "image": images})

def get_id(topic):
    try:
        pid = Post.objects.filter(topic=topic).latest("creation_date").pid
    except Post.DoesNotExist:
        pid = 0

    try:
        rid = Reply.objects.filter(topic=topic).latest("creation_date").rid
    except Reply.DoesNotExist:
        rid = 0

    return pid + rid + 1