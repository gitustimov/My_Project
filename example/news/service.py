from celery.schedules import crontab
from django.core.mail import send_mail

from config.celery import app


def send(user_email):
    app.conf.beat_schedule = {
        'action_every_friday_8am': {
            'task': 'action',
            'schedule': crontab(hour=8, minute=0, day_of_week='friday'),
        },
    }
    send_mail(
        'Вы подписались на рассылку',
        'Вы будете получать рассылку каждую пятницу.',
        'udv0902@yandex.ru',
        [user_email],
        fail_silently=False,
    )
