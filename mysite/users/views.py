from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        messages.add_message(request, messages.SUCCESS,
                             'Hi %s! You successfully registered' % user.username)

        return redirect('thrifts:home')
    else:
        return render(request, 'users/register.html')


def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'users/profile.html', {'user': user})


def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        request.session['username'] = username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully.")
    else:
        messages.add_message(request, messages.ERROR,
                             "Invalid username or password.")
    return redirect('thrifts:home')


def logout_user(request):
    try:
        del request.session['username']
        del request.session['role']
    except KeyError:
        pass
    return redirect('thrifts:home')


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
