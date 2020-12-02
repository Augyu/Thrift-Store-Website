from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.urls import reverse
from .models import Comment


def add_comment(request):
    if is_ajax and request.method == "POST":
        comment = request.POST.get('comment')
        buyer_username = request.session.get('username')
        buyer_id = User.objects.get(username=buyer_username).id
        seller_username = request.POST.get('seller_username')
        seller_id = User.objects.get(username=seller_username).id

        comment = Comment(
            comment=comment, buyer_id=buyer_id, buyer_username=buyer_username, seller_id=seller_id, seller_username=seller_username)
        comment.save()
        data = {'buyer': comment.buyer_username, 'buyer_url': reverse('users:profile', kwargs={'username': comment.buyer_username}),
                'comment': comment.comment, 'date_posted': naturaltime(comment.date_posted), 'id': comment.id}
        return JsonResponse({'success': 'success',
                             'data': data},
                            status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def delete_comment(request):
    if is_ajax and request.method == 'POST':
        comment_id = request.POST.get('id')
        Comment.objects.get(pk=comment_id).delete()
        return JsonResponse({'success': 'success'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def edit_comment(request):
    if is_ajax and request.method == 'POST':
        comment_id = request.POST.get('id')
        comment = Comment.objects.get(pk=comment_id)
        comment.comment = request.POST.get('comment')
        comment.save()
        return JsonResponse({'success': 'success'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid Ajax Request'}, status=400)


def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
