from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import re
from notifications.models import Notify
from nu_talker.models import NuTalker

from posts.forms import PostForm
from posts.models import TalkTalk


#Create your views here.

def talk_view(request, post_id:int):
    speaking = TalkTalk.objects.get(id=post_id)
    return render(request, 'chatpage.html', {'speaking':speaking})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post_create = TalkTalk.objects.create(
                body = data["body"],
                talker_user = request.user
            )
            pattern = re.compile(r'@(\w+)')
            matches = pattern.findall(post_create.body)
            for match in matches:
                if NuTalker.objects.filter(username=match).exists():
                    talk_user = NuTalker.objects.get(username=match)
                    notify = Notify.objects.create(
                        posted = post_create,
                        user = talk_user
                    )
                
    form = PostForm()
    return render(request, "createdpost.html", {"form":form})
