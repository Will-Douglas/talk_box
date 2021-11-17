from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from nu_talker.models import NuTalker
from posts.models import TalkTalk

#Create your views here.

def index(request):

    connection_list = []

    all_posts = TalkTalk.objects.all()
   

    return render(request, "index.html", {"all_posts":all_posts})

def profile(request, user_id: int):
    tha_talker = NuTalker.objects.get(id=user_id)
    all_posts = TalkTalk.objects.filter(talker_user=user_id)
    return render(request, "talkerprofile.html", {"all_posts": all_posts, "tha_talker": tha_talker})