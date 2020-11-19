"""politically_informed URL Configuration

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
from django.urls import path, include

from api.views import *
from authentication.views import *
from electoral_map.views import *
from quiz.views import *
from voters.views import *

urlpatterns = [
    path('', main, name="main"),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('map/', map_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]


# Todo: login_view, logout_view, registration, map_view, api, quiz, edit_profile, main, story, issue

# Todo main: news non-biased
# Todo map: Clickable 270 to win map
# Todo story: news story
# Todo issue: details on certain issue
# Todo suggestion: let people suggest topics or give feedback
# Todo api: data
# Todo quiz: isidewith type quiz but accurate
