from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("index")
        else:
            messages.error(request, "Ім'я або пароль невірні")
    else:
        form = UserCreationForm()

    return render(request, "auth/register.html", context={"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('index')
            else:
                messages.error(request, "Ім'я або пароль невірні")
            
    else:
        form = AuthenticationForm()

    return render(request, "auth/login.html", context={"form": form})

        