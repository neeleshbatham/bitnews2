from django.contrib import admin

from .models import Category, Language, UserProfile

admin.site.register(UserProfile)
admin.site.register(Language)
admin.site.register(Category)