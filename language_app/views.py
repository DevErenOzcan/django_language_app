from django.shortcuts import render
from language_app.models import User


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST["email"])
            if user.password == request.POST["password"]:
                return render(request, "login2.html")
            else:
                return render(request, "loginexcept.html")
        except Exception as e:
            return render(request, "loginexcept.html", e)

    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        try:
            user = User(first_name=request.POST["first_name"],
                        last_name=request.POST["last_name"],
                        email=request.POST["email"],
                        password=request.POST["password"])
            user.save()
            return render(request, "register2.html")
        except Exception as e:
            return render(request, "registerexcept.html", e)
    else:
        return render(request, "register.html")
