from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .forms import *
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'create'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    # {'title': 'Категории', 'url_name': 'categories'},
    # {'title': 'Войти', 'url_name': 'login'},
]


class NewsHome(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


@login_required
def about(request):
    return render(request, 'news/about.html', {'menu': menu, 'title': 'О сайте'})


class Contact(ListView):
    model = News
    template_name = 'news/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Контакты'
        return context


class ShowPost(DetailView):
    model = News
    template_name = 'news/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        # context['cat_selected'] = 0
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    # queryset = Author.objects.all()
    template_name = 'news/authors.html'


class AddNews(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_news',)
    raise_exception = True
    model = News
    form_class = CreateNews
    template_name = 'news/create.html'
    success_url = '/'
    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление статьи'
        # context['cat_selected'] = 0
        return context


class UpdateNews(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_news',)
    raise_exception = True
    model = News
    template_name = 'news/news_edit.html'
    form_class = CreateNews
    success_url = reverse_lazy('home')
    login_url = 'login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Обновление статьи'
        # context['cat_selected'] = 0
        return context


class NewsDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_news',)
    raise_exception = True
    model = News
    template_name = 'news/delnews.html'
    success_url = reverse_lazy('home')
    login_url = 'login'


# Регистрация пользователя
class RegisterUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'news/register.html'
    # success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Регистрация'
        # context['cat_selected'] = 0
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


#  Авторизация пользователя
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'news/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Авторизация'
        # context['cat_selected'] = 0
        return context

    def get_success_url(self):
        return reverse_lazy('home')


# Выход пользователя
def logout_user(request):
    logout(request)
    return redirect('login')
