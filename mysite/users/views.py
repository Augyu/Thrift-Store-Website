from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from .models import Details
from datetime import datetime
from django.urls import reverse
from comments.models import Comment
from feeds.models import Feed


def register(request):
    if request.method == 'POST':
        if is_ajax:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            first_name = request.POST.get('fName')
            last_name = request.POST.get('lName')
            birth = request.POST.get('birth')
            user = User.objects.create_user(
                username, email, password, first_name=first_name, last_name=last_name)
            detail = Details.objects.get(user_id=user.id)
            detail.birth = datetime.strptime(birth, '%Y-%m-%d')
            detail.save()
            request.session['username'] = username
            request.session['role'] = user.details.role
            feed = Feed(user=user, verb='has just signed up', target=user)
            feed.save()
            return JsonResponse({'success': 'success', 'data': {'url': reverse('thrifts:home')}}, status=200)
        else:
            return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)
    else:
        return render(request, 'users/register.html')


def edit(request, username):
    if request.method == 'POST':
        if is_ajax:
            user = User.objects.get(username=username)
            user.first_name = request.POST.get('fName')
            user.last_name = request.POST.get('lName')
            user.email = request.POST.get('email')
            user.details.birth = request.POST.get('birth')
            user.save()
            return JsonResponse({'success': 'success', 'data': {'url': reverse('users:profile', args=[username])}}, status=200)
        else:
            return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)
    else:
        user = User.objects.get(username=username)
        birth = user.details.birth
        birth = birth.strftime("%Y-%m-%d")
        return render(request, 'users/edit.html', {'user': user, 'birth': birth})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    birth = user.details.birth
    birth = birth.strftime("%Y-%m-%d")
    comments = Comment.objects.filter(seller_username=username)
    feeds = Feed.objects.filter(user=user).order_by('-created_time')[:10]
    return render(request, 'users/profile.html', {'user': user, 'birth': birth, 'comments': comments, "feeds": feeds})


def login_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        request.session['username'] = username
        request.session['role'] = user.details.role
        messages.add_message(request, messages.SUCCESS,
                             "You have logged in successfully.")
        feed = Feed(user=user, verb='has just logged in', target=user)
        feed.save()
    else:
        messages.add_message(request, messages.ERROR,
                             "Invalid username or password.")
    return redirect('thrifts:home')


def logout_user(request):
    try:
        user = User.objects.get(username=request.session['username'])
        feed = Feed(user=user, verb='has just logged out', target=user)
        del request.session['username']
        del request.session['role']
        feed.save()
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
