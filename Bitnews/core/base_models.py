from datetime import datetime
from django.db import models
from django.conf import settings


def set_user_pic_path(instance, filename):
    return '{0}/{1}/user'.format(settings.ENV, settings.BRAND)


class BaseModel(models.Model):
    """
    Base model contains created date and modified date
    """
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(BaseModel):
    '''User profile model to extend User'''

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    device_id = models.CharField(max_length=50, unique=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    pincode = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    
    # is_lang_accepted = models.BooleanField(default=False)
    # is_cat_accepted = models.BooleanField(default=False)

    image_url = models.ImageField(upload_to='user-images',
                                  max_length=200, null=True, blank=True)
#                                   validators=[validate_image])

    # def image_tag(self):
    #     return u'<img src="{0}/{1}" width="200px;"/>'.format(settings.S3_BASE_URL, self.image_url)
    # image_tag.short_description = 'User Image'
    # image_tag.allow_tags = True

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Other'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES,
                              blank=True, null=True)

    class Meta:
        db_table = "bn_userprofile"
        verbose_name_plural = "User Profile"
        abstract = True

    def __unicode__(self):
        return str(self.phone_number or '') + ' ' + self.user.username

class Category(BaseModel):
    ''' Interests Categories '''
    
    name = models.CharField(max_length=100,null=True, blank=True)
    image_url = models.ImageField(upload_to='category-images',
                                  max_length=200, null=True, blank=True)
    class Meta:
        db_table = "bn_category"
        verbose_name_plural = "Interests Category"
        abstract = True

    def __unicode__(self):
        return str(self.name)

class Language(BaseModel):
    '''Stores the different languages for the user'''
    name = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to='languages-images',
                                  max_length=200, null=True, blank=True)

    class Meta:
        abstract = True
        db_table = "bn_language"
        verbose_name_plural = "Languages"

    def __unicode__(self):
        return self.name    

class News(BaseModel):
    '''Stores the different languages for the user'''

    class Meta:
        abstract = True
        db_table = "bn_news"

    def __unicode__(self):
        return self.title 