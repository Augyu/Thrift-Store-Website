from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from .models import Details
from datetime import datetime
from django.urls import reverse


def register(request):
    if is_ajax and request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('fName')
        last_name = request.POST.get('lName')
        birth = request.POST.get('birth')
        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)
        # messages.add_message(request, messages.SUCCESS,
        #                      'Hi %s! You successfully registered' % user.username)
        detail = Details.objects.get(user_id=user.id)
        detail.birth = datetime.strptime(birth, '%Y-%m-%d')
        detail.save()
        request.session['username'] = username
        request.session['role'] = user.details.role
        return JsonResponse({'success': 'success', 'data': {'url': reverse('thrifts:home')}}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


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


def list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})


def change_role(request):
    if is_ajax and request.method == 'POST':
        id = request.POST.get('id')
        role = request.POST.get('role')
        user = User.objects.get(pk=id)
        detail = user.details
        detail.role = role
        detail.save()
        messages.add_message(request, messages.SUCCESS,
                             "You have changed successfully.")
        return JsonResponse({'success': 'success', 'data': {'url': reverse('users:list')}}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
