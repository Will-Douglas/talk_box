from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import nu_talker

from nu_talker.models import NuTalker
from posts.models import TalkTalk

#Create your views here.
@login_required
def index(request):

    connection_list = []

    all_posts = TalkTalk.objects.all()
    for post in all_posts:
        if post.spokesmen in request.user.connection.all() or post.spokesmen == request.user:
            connection_list.append(post)
    connection_list.sort(key=lambda x: x.talk_stated, reverse=True)
    return render(request, "index.html", {"all_post": all_posts, "connection_list": connection_list})
   

    return render(request, "index.html", {"all_posts":all_posts})

def profile(request, user_id: int):
    tha_talker = NuTalker.objects.get(id=user_id)
    all_posts = TalkTalk.objects.filter(spokesmen = user_id)
    return render(request, "talkerprofile.html", {"all_posts": all_posts, "tha_talker": tha_talker})

def ConnectionView(request, user_id: int):
    connected = NuTalker.objects.get(id=user_id)
    if request.user.is_authenticated:
        auth_user = NuTalker.objects.get(id=request.user.id)
        auth_user.connected.add(connected)
        auth_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def DisconnectionView(request, user_id: int):
    connected = NuTalker.objects.get(id=user_id)
    if request.user.is_authenticated:
        auth_user = NuTalker.objects.get(id=request.user.id)
        auth_user.connected.remove(connected)
        auth_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


