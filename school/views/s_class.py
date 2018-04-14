from datetime import datetime
from django.http import Http404

from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend

# Importing Serializers
from ..Serializers.sclass import ClassModelSerializer

# Importing models
from ..models.sclass import ClassModel

#Importing Filters
from ..filters.sclass import ClassFilter

class ClassModelView(ModelViewSet):
    serializer_class = ClassModelSerializer
    queryset = ClassModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = ClassFilter

    @list_route(methods=['get'])
    def count(self, *args, **kwargs):
        staff_count = ClassModel.objects.count()
        return Response(status=status.HTTP_200_OK, data={"count":staff_count})
