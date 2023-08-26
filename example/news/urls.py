from django.urls import path, include
from .views import *

urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    # path('category/<int:cat_id>/', NewsCategory.as_view(), name='categories'),
    path('contact/', Contact.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('authorlist/', AuthorList.as_view()),
    # path('post/<int:pk>/', Post.as_view()),
    path('register/', RegisterUser.as_view(), name='register'),
    path('create/', AddNews.as_view(), name='create'),
    path('post/<int:pk>/delete/', NewsDeleteView.as_view(), name='delnews'),
    path('post/<int:pk>/update', UpdateNews.as_view(), name='news_edit'),

]

