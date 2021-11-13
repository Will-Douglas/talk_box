from django.shortcuts import render

from posts.models import TalkTalk

# Create your views here.
def talk_view(request, post_id:int):
    speaking = TalkTalk.objects.get(id=post_id)
    return render(request, 'chatpage.html', {'speaking':speaking})