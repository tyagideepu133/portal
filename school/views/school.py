from datetime import datetime
from django.http import Http404

from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend

from ..Serializers.school import (SchoolModelSerializer)                                    
from ..models.school import SchoolModel
from django.contrib.auth.models import User
from ..filters.school import SchoolFilter



class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
    
class SchoolModelView(CreateListMixin, ModelViewSet):
    serializer_class = SchoolModelSerializer
    queryset = SchoolModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = SchoolFilter

    @list_route(methods=['get'])
    def count(self, *args, **kwargs):
        school_count = SchoolModel.objects.count()
        return Response(status=status.HTTP_200_OK, data={"count":school_count})
