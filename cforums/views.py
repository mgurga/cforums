
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone

from .forms import PostForm

from .models import Post
from .models import Image

def home_view(request):
    return render(request, "home.html", {"topics": settings.TOPICS, "forumtitle": settings.TITLE})

def post_form(request, topic):
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
                reply_to=0,
                topic=topic,
                body=form.cleaned_data["body"],
                creation_date=timezone.now(),
            )

            newpost.images.add(postimage)

            newpost.save()

            return HttpResponseRedirect("/topic/" + topic)
    else:
        form = PostForm()

    return render(request, "postform.html", {"form": form, "topic": topic})

def reply_form(request, topic, id):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            postimage = Image.objects.create(
                file=request.FILES["image"],
                filename=request.FILES["image"].name
            )

            postimage.save()

            newrep = Post.objects.create(
                pid=get_id(topic),
                reply_to=id,
                title=form.cleaned_data["title"],
                pinned=False,
                topic=topic,
                body=form.cleaned_data["body"],
                creation_date=timezone.now(),
            )

            newrep.images.add(postimage)

            newrep.save()

            return HttpResponseRedirect("/topic/" + topic)
    else:
        form = PostForm()

    return render(request, "replyform.html", {"form": form, "topic": topic, "id": id})

def post_view(request, topic, id):
    post = Post.objects.filter(topic=topic).get(pid=id)
    images = post.images.all().first()
    return render(request, "post.html", {"topic": topic, "post": post, "image": images})

def replies_view(request, topic, id):
    replies = Post.objects.filter(reply_to=id)
    replyout = []
    for reply in replies:
        simplereply = {
            "title": reply.title,
            "id": reply.pid,
            "creation_date": reply.creation_date
        }
        replyout.append(simplereply)
    return render(request, "postreplies.html", {"replies": replyout})

def get_id(topic):
    try:
        pid = Post.objects.filter(topic=topic).latest("creation_date").pid
    except Post.DoesNotExist:
        pid = 0

    return pid + 1