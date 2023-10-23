import datetime

from celery import shared_task

from .models import Post, Category
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_weekly_posts_list():
    today = datetime.datetime.now()
    print(today)
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(post_created__gte=last_week)
    categories = set(posts.values_list('categories__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    print(subscribers)

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def send_new_post_notification(pk):
    post = Post.objects.get(pk=pk)
    categs = post.categories.all()
    subscribers_email = []

    for cat in categs:
        subscribers = cat.subscribers.all()
        subscribers_email += [s.email for s in subscribers]

    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': post.preview,
            'link': f'{settings.SITE_URL}/news/{post.pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=post.title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers_email,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
