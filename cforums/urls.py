"""cforums URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

from .views import home_view
from .views import post_form
from .views import post_view
from .views import replies_view
from .views import reply_form

from cforums.topic.views import TopicView

faviconredir = RedirectView.as_view(url='/static/favicon.ico')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('favicon.ico', faviconredir),
    path('topic/<str:topic>/', TopicView.as_view()),
    path('topic/<str:topic>/post', post_form),
    path('topic/<str:topic>/<int:id>', post_view),
    path('topic/<str:topic>/<int:id>/reply', reply_form),
    path('topic/<str:topic>/<int:id>/replies', replies_view)
]
