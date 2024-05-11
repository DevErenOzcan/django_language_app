import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from language_app.models import User


@login_required(login_url=reverse_lazy("login"))
def home(request):
    return render(request, "home.html")


def login_page(request):
    if request.method == "POST":
        response_data = {}
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_object = User.objects.get(email=email)
        except ObjectDoesNotExist:
            user_object = None

        if user_object is None:
            response_data["error"] = True
            response_data["result"] = "Email or password is wrong"
        else:
            user = authenticate(email=email, password=password)

            if user is None:
                response_data["error"] = True
                response_data["result"] = "Email or password is wrong"
            else:
                login(request, user)

                response_data["error"] = False
                response_data["result"] = ""

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        response_data = {}
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_object = User.objects.get(email=email)
        except ObjectDoesNotExist:
            user_object = None

        if user_object is None:
            user = User.objects.create(email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            response_data["error"] = False
            response_data["result"] = "Kullanıcı başarı ile oluşturuldu"
        else:
            response_data["error"] = True
            response_data["result"] = "Email already exists"

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render(request, "register.html")


def forgot_password_page(request):
    if request.method == "POST":
        response_data = {}
        email = request.POST.get("email")

        try:
            user_object = User.objects.get(email=email)
        except ObjectDoesNotExist:
            user_object = None

        if user_object is None:
            response_data["error"] = True
            response_data["result"] = "Email not found"
        else:
            response_data["error"] = False
            response_data["result"] = "We sent an email to your email address. Please check your inbox."

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render(request, "forgot_password.html")
