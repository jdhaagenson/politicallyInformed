from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse

from .forms import *

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", reverse("main")))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("main"))


@login_required
def register_view(request):
    if request.method == 'POST':
        form = RegisterVoter(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Voter.objects.create(email=data['email'],
                                 username=data['username'],
                                 password=data['password'],
                                 gender=data['gender'],
                                 )