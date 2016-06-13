from tastypie.resources import Resource, ModelResource
from tastypie.utils.mime import determine_format
from tastypie.http import HttpBadRequest
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.fields import ApiField
from tastypie import http
from django.http.response import HttpResponse
from django.conf import settings


class BaseCorsResource(Resource):
    """
    Class implementing CORS
    """
    def create_response(self, *args, **kwargs):
        response = super(BaseCorsResource, self).create_response(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    def method_check(self, request, allowed=None):
        if allowed is None:
            allowed = []

        request_method = request.method.lower()
        for i,method in enumerate(allowed):
            allowed[i] = method.encode('ascii','ignore')
        allows = ','.join(map(str.upper, allowed))

        if request_method == 'options':
            response = HttpResponse(allows)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        if not request_method in allowed:
            response = http.HttpMethodNotAllowed(allows)
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        return request_method


class CustomBaseModelResource(BaseCorsResource, ModelResource):
    def determine_format(self, request):
        """
        return application/json as the default format
        """
        fmt = determine_format(request, self._meta.serializer,\
                               default_format=self._meta.default_format)
        if fmt == 'text/html' and 'format' not in request:
            fmt = 'application/json'
        return fmt
    
    def dispatch(self, request_type, request, **kwargs):
        if self._meta and hasattr(self._meta, 'queryset'):
            if settings.BRAND in settings.OUTSIDE_BRANDS:
                model = get_model(self._meta.queryset.model.__name__,)
                setattr(self._meta, 'object_class', model)
        return super(CustomBaseModelResource, self).dispatch(request_type, request, **kwargs)
 
    def get_object_list(self, request):
        if settings.BRAND in settings.OUTSIDE_BRANDS:
            return get_model(self._meta.queryset.model.__name__,).objects.all()
        return self._meta.queryset._clone()