"""Bitnews URL Configuration
"""

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from tastypie.api import Api
from core import user_api, scrap_api
from core import urls


admin.autodiscover()

api_v1 = Api(api_name="v1")

api_v1.register(user_api.BitUserResource()),
api_v1.register(user_api.NewsResource())


urlpatterns = [
    url(r'', include(api_v1.urls)),           
    url(r'^admin/', admin.site.urls),
    url(r'^bitnews/', include(urls)),
    url(r'^$', include(urls)),
    url(r'^read/', scrap_api.read_file, name='read_file'),
    url(r'^news-to-feeds/', user_api.news_to_feeds, name='news_to_feeds'),
    url(r'^user-feeds/', user_api.feeds_to_user, name='feeds_to_user'),
    url(r'^interest_update/', user_api.interest_update, name='interest_update'),
]
