# from allauth.account.utils import user_email
from celery import shared_task
from django.contrib.auth.models import User

from config.celery import app
from django.core.mail import send_mail
from .service import send


@shared_task
def send_beat_email(user_email):
    send(user_email)

# @app.task
# def send_beat_email():
#     for user in User.objects.all():
#         send_mail(
#             'Вы подписались на рассылку',
#             'Вы будете получать рассылку каждую пятницу.',
#             'udv0902@yandex.ru',
#             [user_email],
#             fail_silently=False,
#         )
