from django.db import models
from django.contrib.auth.models import User
from core import base_models

_APP_NAME ='core'

class Category(base_models.Category):

    class Meta(base_models.Category.Meta):
        app_label = _APP_NAME


class Language(base_models.Language):

    class Meta(base_models.Language.Meta):
        app_label = _APP_NAME


class UserProfile(base_models.UserProfile):
    user = models.OneToOneField(User, primary_key=True,
                                        related_name='core_users')

    interests_category = models.ManyToManyField(Category)
    user_languages = models.ManyToManyField(Language)
    
    class Meta(base_models.UserProfile.Meta):
        app_label = _APP_NAME
