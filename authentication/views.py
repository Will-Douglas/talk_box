from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

from nu_talker.models import NuTalker
from posts.models import TalkTalk

from authentication.forms import LogInForm, SignUpForm


# Create your views here.
def LoginView(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            talker = authenticate(
                username=data['username'], password=data['password'])
            if talker:
                login(request, talker)
                return HttpResponseRedirect(reverse("Homepage"))

    form = LogInForm()
    return render(request, 'signupform.html', {'form':form})


def TalkLogOut(request):
    logout(request)
    return HttpResponseRedirect(reverse("Homepage"))