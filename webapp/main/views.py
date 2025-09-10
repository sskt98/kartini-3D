from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Photo
from django.shortcuts import render, get_object_or_404
import os
import re

from .forms import SignUpForm

def about(request):
    photos = list(Photo.objects.all())

    def get_number(photo):
        name = os.path.splitext(os.path.basename(photo.image.name))[0]
        match = re.search(r'\d+', name)
        return int(match.group()) if match else 0

    photos.sort(key=get_number)
    return render(request, 'main/about.html', {'photos': photos})

def page(request):
    print(request.user)


def index(request):
    return render(request, 'main/index.html')




def contact(request):
    return render(request, 'main/contact.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неправильне ім''я користувача або пароль.')
    return render(request, 'main/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Ви успішно зареєструвалися!')
            return redirect('home')
        else:
            messages.error(request, 'Перевірте форму: є помилки.')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'main/photo_detail.html', {'photo': photo})

