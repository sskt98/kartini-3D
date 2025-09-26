from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import SignUpForm
import re


def about(request):
    photos = list(Photo.objects.all())


    def get_number(photo):
        public_id = getattr(photo.image, 'public_id', None)
        if public_id:
            match = re.search(r'R-(\d+)', public_id)
            return int(match.group(1)) if match else 0
        else:
            return photo.id

    photos.sort(key=get_number)
    return render(request, 'main/about.html', {'photos': photos})


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'main/photo_detail.html', {'photo': photo})


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
            messages.error(request, "Неправильне ім'я користувача або пароль.")
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

def page(request):
    print(request.user)
    return render(request, 'main/page.html')