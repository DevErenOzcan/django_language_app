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
            user = authenticate(username=email, password=password)

            if user is None:
                if user_object.is_active:
                    response_data["error"] = True
                    response_data["result"] = "Email or password is wrong"
                else:
                    response_data["error"] = True
                    response_data["result"] = "Account not activated"
            else:
                login(request, user)

                response_data["error"] = False
                response_data["result"] = ""

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render(request, "login.html")

