from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Вы будете получать рассылку каждую пятницу.',
        'udv0902@yandex.ru',
        [user_email],
        fail_silently=False,
    )
