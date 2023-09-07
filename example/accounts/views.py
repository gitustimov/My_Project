from django.views.generic import CreateView
from .models import ContSub
# from .forms import ContactForm
# from news.service import send
# from news.tasks import send_beat_mail
#
#
# class ContactView(CreateView):
#     model = ContSub
#     form_class = ContactForm
#     template_name = 'news/subscr.html'
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.save()
#         send(form.instance.email)
#         send_beat_mail.delay(form.instance.email)
#         return super().form_valid(form)
