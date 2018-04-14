from datetime import datetime
from django.http import Http404

from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend

from ..Serializers.student import (StudentModelSerializer)                                    
from ..models.student import StudentModel
from django.contrib.auth.models import User
from django_filters import FilterSet, NumberFilter  
from ..filters.student import StudentFilter

class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

# class StudentFilter(FilterSet):
#     class Meta:
#         model = StudentModel
#         fields = '__all__'
    
class StudentModelView(CreateListMixin, ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = StudentModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = StudentFilter

    @list_route(methods=['get'])
    def count(self, *args, **kwargs):
        student_count = StudentModel.objects.count()
        return Response(status=status.HTTP_200_OK, data={"count":student_count})
