from celery import shared_task
from django.contrib.auth.models import User
from .models import Post, Response
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone


@shared_task
def send_mail_monday_8am():
    now = timezone.now()
    list_week_posts = list(Post.objects.filter(dateCreation__gte=now - timedelta(days=7)))
    if list_week_posts:
        for user in User.objects.filter():
            print(user)
            post_list = ''
            for post in list_week_posts:
                post_list += f'\n{post.title}\nhttp://127.0.0.1:8000/post/{post.id}'
            send_mail(
                subject=f'Все объявления за прошедшую неделю.',
                message=f'Здравствуйте, {user.username}!\n Ознакомьтесь с новыми объявлениями на нашем сайте, '
                        f'появившимися за прошедшую неделю:\n{post_list}',
                from_email='123@mail.ru',
                recipient_list=[user.email],
            )