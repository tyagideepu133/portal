from datetime import datetime
from django.http import Http404

from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend


from ..Serializers.marks import (ExamModelSerializer, StudentMarksModelSerializer, SubjectMarkSerializer)
from ..models.marks import (ExamModel, StudentMarksModel, SubjectMarkModel)
from ..filters.marks import ExamFilter, SubjectMarkFilter, StudentMarksFilter

class ExamModelView(ModelViewSet):
    serializer_class = ExamModelSerializer
    queryset =ExamModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = ExamFilter

class SubjectMarkView(ModelViewSet):
    serializer_class = SubjectMarkSerializer
    queryset = SubjectMarkModel.objects.all()
    # detail_serializer_class = SubjectMarkSerializerDetail
    filter_backends = (DjangoFilterBackend,)
    filter_class = SubjectMarkFilter

    @list_route(methods=['get'])
    def student_view(self, *args, **kwargs):
        subjectMarks = SubjectMarkModel.objects.all()
        serializer = SubjectMarkSerializer(subjectMarks, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         if hasattr(self, 'detail_serializer_class'):
    #             return self.detail_serializer_class
    #     return super(SubjectMarkView, self).get_serializer_class()

class StudentMarkView(ModelViewSet):
    serializer_class = StudentMarksModelSerializer
    queryset = StudentMarksModel.objects.all()
    # detail_serializer_class = SubjectMarkSerializerDetail
    filter_backends = (DjangoFilterBackend,)
    filter_class = StudentMarksFilter