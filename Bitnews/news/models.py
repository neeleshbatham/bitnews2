from django.db import models
from django.conf import settings
from core.base_models import Category, Language, News

_APP_NAME = "news"

class NewsCategory(Category):

    class Meta:
        app_label = _APP_NAME
        verbose_name_plural = "News Interests Category"


class NewsLanguage(Language):

    class Meta:
        app_label = _APP_NAME
        verbose_name_plural = "News Languages"


class News(News):
    '''News model extended by News in Base Model'''	

    language = models.ForeignKey(NewsLanguage,null=True)
    category= models.ForeignKey(NewsCategory,null=True)

    source = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.CharField(max_length=200, blank=False, default=None)
    pubdate=models.DateTimeField(null=True, blank=True,editable=False)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True)
    link = models.CharField(max_length=200,null=True, blank=True)
    
    class Meta(News.Meta):
        app_label = _APP_NAME
        verbose_name_plural = "News"

        def __unicode__(self):
        	return u'%s' % (self.title)
