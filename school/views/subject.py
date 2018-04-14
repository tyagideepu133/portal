from datetime import datetime
from django.http import Http404

from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from django_filters.rest_framework import DjangoFilterBackend

from ..Serializers.subject import (SubjectModelSerializer)

from ..models.subject import (SubjectModel)

from ..filters.subject import SubjectFilter

class SubjectModelView(ModelViewSet):
    serializer_class = SubjectModelSerializer
    queryset = SubjectModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = SubjectFilter

