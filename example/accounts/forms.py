from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail, EmailMultiAlternatives, mail_managers, mail_admins


# class CustomSignupForm(SignupForm):
#     def save(self, request):
#         user = super().save(request)
#         common_users = Group.objects.get(name="common users")
#         user.groups.add(common_users)
#         send_mail(
#             subject='Добро пожаловать в наш новостной сайт!',
#             message=f'{user.username}, вы успешно зарегистрировались!',
#             from_email=None,
#             recipient_list=[user.email],
#         )
#         return user

class CustomSignupForm(SignupForm):
    # Добавление пользователя в группу common_users
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)

        # Заголовок и текст письма
        subject = 'Добро пожаловать на новостной сайт.'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/">сайте My project</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        # Рассылка писем менеджерам сайта и админам
        mail_managers(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )
        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )
        return user
