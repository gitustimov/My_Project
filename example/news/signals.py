from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import News


@receiver(post_save, sender=News)
def news_created(instance, created, **kwargs):
    if not created:
        return

    # emails = User.objects.filter(subscriptions__cat=instance.cat).values_list('email', flat=True)
    emails = User.objects.all().values_list('email', flat=True)
    subject = f'Новая запись в категории {instance.cat}'

    text_content = (
        f'Новость: {instance.title}\n'
        f'Ссылка на новость:href=http://127.0.0.1{instance.get_absolute_url()}'
    )
    html_content = (
        f'Новость: {instance.title}<br>'
        f'Ссылка на новость:href=http://127.0.0.1{instance.get_absolute_url()}'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
