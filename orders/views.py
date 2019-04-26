from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user
        }
    else:
        context = {
            "user": None
        }
    return render(request, "orders/index.html", context)

def login_view(request):
    if request.method == 'POST':
        try:
            username = request.POST["username"]
        except KeyError:
            return render(request, "orders/login.html", {"message": "Missing username"})
        else:
            try:
                password = request.POST["password"]
            except KeyError:
                return render(request, "orders/login.html", {"message": "Missing password"})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials"})
    else:
        return render(request, "orders/login.html", {"message": None})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out"})

def register_view(request):
    if request.method == 'POST':
        # check they provided all info and collect it
        user_info = dict()
        for key in ['username', 'first_name', 'last_name', "email", "pass1", "pass2"]:
            if not request.POST[key]:
                return render(request, "orders/register.html", {"message": f"Missing {key}"})
            else:
                user_info[key] = request.POST[key]
        # check passwords match
        if user_info["pass1"] != user_info["pass2"]:
            return render(request, "orders/register.html", {"message": "Passwords don't match"})
        # create the new user
        try:
            new_user = User.objects.create_user(
                username=user_info["username"],
                first_name=user_info["first_name"],
                last_name=user_info["last_name"],
                password=user_info["pass1"],
                email=user_info["email"],
                is_staff=False
            )
            new_user.save()
        except:
            return HttpResponseServerError("There was a problem creating the new user")
        # log user in and redirect to index
        user = authenticate(request, username=user_info["username"], password=user_info["pass1"])
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    # if coming via GET, serve registration form
    else:
        return render(request, "orders/register.html")

