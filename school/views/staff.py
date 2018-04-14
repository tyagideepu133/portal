from datetime import datetime
from django.http import Http404

from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend

from ..Serializers.staff import (StaffModelSerializer)                                    
from ..models.staff import StaffModel
from ..filters.staff import StaffFilter
from django.contrib.auth.models import User
from django_filters import FilterSet, NumberFilter  

class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

class StaffFilter(FilterSet):
    class Meta:
        model = StaffModel
        fields = '__all__'
    
class StaffModelView(CreateListMixin, ModelViewSet):
    serializer_class = StaffModelSerializer
    queryset = StaffModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = StaffFilter

    @list_route(methods=['get'])
    def count(self, *args, **kwargs):
        staff_count = StaffModel.objects.count()
        return Response(status=status.HTTP_200_OK, data={"count":staff_count})
