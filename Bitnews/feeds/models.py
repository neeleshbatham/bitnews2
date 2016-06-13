from django.db import models
from django.conf import settings
from core.base_models import UserProfile

_APP_NAME = "feeds"


class NewsFeedItems(models.Model):
    
    language = models.CharField(max_length=100,null=True, blank=True)
    category= models.CharField(max_length=100,null=True, blank=True)

    source = models.CharField(max_length=100,null=True, blank=True)
    image_url = models.CharField(max_length=200,null=True, blank=True)
    pubdate=models.DateTimeField(null=True, blank=True,editable=False)
    title = models.CharField(max_length=200,null=True, blank=True)
    content = models.TextField(null=True)
    link = models.CharField(max_length=200,null=True, blank=True)

    class Meta:
        app_label = _APP_NAME
        verbose_name_plural = "News Feed Items"

        def __unicode__(self):
        	return u'%s' % (self.title)



class ProductItems(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	pub_date = models.CharField(max_length=200)

	class Meta:
		app_label = _APP_NAME
		verbose_name_plural = "Products Items"

class Feeds(models.Model):
	user = models.ForeignKey(UserProfile)
	news_items = models.ManyToManyField(NewsFeedItems, blank=True)
	# product_item = models.ManyToManyField(ProductItems, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
		
	class Meta:
		app_label = _APP_NAME
		verbose_name_plural = "Feeds"