from django.contrib import admin
from .models import *

admin.site.register(News)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)


@admin.register(ContSub)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
