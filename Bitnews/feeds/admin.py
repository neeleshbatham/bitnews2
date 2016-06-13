from django.contrib import admin

from .models import NewsFeedItems, ProductItems, Feeds

class NewsFeedItemsAdmin(admin.ModelAdmin):
    list_display = ("title","pubdate","category", "language" )
    search_fields = ('title','language', 'category')



admin.site.register(NewsFeedItems,NewsFeedItemsAdmin)
admin.site.register(ProductItems)
admin.site.register(Feeds)
