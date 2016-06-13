from django.conf.urls import patterns, url, include
from django.conf import settings
from tastypie.api import Api
from core import user_api

api_v1 = Api(api_name="v1")

api_v1.register(user_api.BitUserResource())

urlpatterns = patterns('',
    url(r'', include(api_v1.urls)),
)
