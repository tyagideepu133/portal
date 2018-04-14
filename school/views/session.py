from datetime import datetime
from django.http import Http404

from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend

from ..Serializers.session import (SessionModelSerializer, ClassSessionModelSerializer, StudentSessionModelSerializer,
                        SubjectSessionModelSerializer, SubjectTimingModelSerializer)

from ..models.session import (SessionModel, ClassSessionModel, StudentSessionModel, SubjectSessionModel, SubjectTimingModel)

from ..filters.session import SessionFilter, ClassSessionFilter, StudentSessionFilter, SubjectSessionFilter, SubjectTimingFilter

class SessionModelView(ModelViewSet):
    serializer_class = SessionModelSerializer
    queryset = SessionModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = SessionFilter 

    @list_route(methods=['get'])
    def count(self, *args, **kwargs):
        session_count = SessionModel.objects.count()
        return Response(status=status.HTTP_200_OK, data={"count":session_count})

class ClassSessionView(ModelViewSet):
    serializer_class = ClassSessionModelSerializer
    queryset = ClassSessionModel.objects.all()
    # detail_serializer_class = ClassSessionSerializerDetail
    filter_backends = (DjangoFilterBackend,)
    filter_class = ClassSessionFilter

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         if hasattr(self, 'detail_serializer_class'):
    #             return self.detail_serializer_class
    #     return super(ClassSessionView, self).get_serializer_class()

class StudentSessionsView(ModelViewSet):
    serializer_class = StudentSessionModelSerializer
    queryset = StudentSessionModel.objects.all()
    # detail_serializer_class = StudentSessionSerializerDetail
    filter_backends = (DjangoFilterBackend,)
    filter_class = StudentSessionFilter

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         if hasattr(self, 'detail_serializer_class'):
    #             return self.detail_serializer_class
    #     return super(StudentSessionsView, self).get_serializer_class()

class SubjectSessionView(ModelViewSet):
    serializer_class = SubjectSessionModelSerializer
    queryset = SubjectSessionModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = SubjectSessionFilter
    # detail_serializer_class = SubjectSessionSerializerDetail

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         if hasattr(self, 'detail_serializer_class'):
    #             return self.detail_serializer_class
    #     return super(SubjectSessionView, self).get_serializer_class()

class SubjectTimingView(ModelViewSet):
    serializer_class = SubjectTimingModelSerializer
    queryset = SubjectTimingModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = SubjectTimingFilter
    # detail_serializer_class = SubjectTimingSerializerDetail

    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         if hasattr(self, 'detail_serializer_class'):
    #             return self.detail_serializer_class
    #     return super(SubjectTimingView, self).get_serializer_class()