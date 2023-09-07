from celery import shared_task
from .service import send


@shared_task
def send_beat_email(user_email):
    send(user_email)
