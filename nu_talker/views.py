from django.shortcuts import render, HttpResponseRedirect

from posts.models import TalkTalk

# Create your views here.
def index(resquest):
    all_posts = TalkTalk.objects.all()
    return render(request, "index.html", {"all_posts":all_posts})