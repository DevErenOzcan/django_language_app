from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy


@login_required(login_url=reverse_lazy("login"))
def home(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "home.html")


@login_required(login_url=reverse_lazy("login"))
def test(request):
    return render(request, "test.html")

