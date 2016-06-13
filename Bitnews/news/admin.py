from django.contrib import admin

from .models import NewsCategory, NewsLanguage, News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title","pubdate","category", "language" )
    search_fields = ('language__name', 'category__name')


admin.site.register(NewsLanguage)
admin.site.register(NewsCategory)
admin.site.register(News,NewsAdmin)
