import json
import logging
from datetime import datetime, date
import pytz

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.http import HttpBadRequest
from tastypie.utils.urls import trailing_slash

from django.conf import settings
from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.http.response import HttpResponse
from django.db.models.query_utils import Q
from django.db.transaction import atomic
from django.forms.models import model_to_dict

from apis.base_api import CustomBaseModelResource
from utils import generate_unique_customer_id
from core.models import UserProfile


class DjangoUserResources(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        authentication = AccessTokenAuthentication()
        validation = UserValidation()
        authorization = MultiAuthorization(Authorization(), CustomAuthorization())
        allowed_methods = ['get', 'post', 'put']
        excludes = ['password', 'is_superuser']
        always_return_data = True

class BitUserResource(CustomBaseModelResource):

    user = fields.ForeignKey(DjangoUserResources, 'user', null=True, blank=True, full=True)

    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = "bitusers"
        authentication = AccessTokenAuthentication()
        validation = ConsumerValidation()
        authorization = MultiAuthorization(Authorization(), CustomAuthorization())
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put']
        always_return_data = True
        filtering = {
                     "consumer_id": ALL
                     }

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/registration%s" % (self._meta.resource_name, trailing_slash()), self.wrap_view('user_registration_phone'), name="user_registration"),
            url(r"^(?P<resource_name>%s)/registration/email%s" % (self._meta.resource_name, trailing_slash()), self.wrap_view('user_registration_email'), name="user_registration_email"),

			]


    def create_user(self, is_active, device_id, email=None):
        consumer_id = generate_unique_customer_id()
        password = consumer_id+settings.PASSWORD_POSTFIX
        user_obj = User.objects.create(username=consumer_id)
        user_obj.set_password(password)
        user_obj.is_active = is_active
        if email:
            user_obj.email=email
        user_obj.save(using=settings.BRAND)
        bituser_obj = UserProfile(user=user_obj,device_id=device_id)
                                                              
        bituser_obj.save()
        return {'bituser_obj': bituser_obj}

    def user_registration(self, request, **kwargs):
        '''
        Register user with valid device id
        Args : device id
        '''
        device_id = request.GET['device_id']
        if not device_id:
            return HttpBadRequest("Enter device id")
        try:

            bituser = UserProfile.objects.filter(device_id = device_id)
            details = []
            if bituser:
                data = {}
                user_language_variable_dict = map(model_to_dict, userbit.user_language.all())
            
                data['user_interest'] = bituser.interests_category
                data['user_language'] = bituser.user_language
                details.append(data)
            data = {'status_code':200,'bituser_details': details}
        
        except Exception as ObjectDoesNotExist:
            logger.info('Exception while fetching user - {0}'.format(device_id))
            try:
                user_obj = self.create_user(True, device_id=device_id)
                bituser_obj = user_obj['bituser_obj']
                data = {'status':1, 'message': 'Phone number registered successfully'}
                return HttpResponse(json.dumps(data), content_type="application/json")
            
            except Exception as ex:
                    logger.info("Exception while registering user with device id - {0}".format(ex))
                    return HttpBadRequest("Device could not be registered")
 




