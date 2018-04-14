from datetime import datetime
from django.http import Http404
from rest_framework.views import APIView, Response, status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import list_route
from django_filters.rest_framework import DjangoFilterBackend
import urllib.request
import urllib.parse

from django.db.models.functions import ExtractWeek
from django.db.models import Count


# Importing Serializers
from ..Serializers.attendence import StudentAttendenceModelSerializer

# Importing models
from ..models.attendence import StudentAttendenceModel

# Importing filters
from ..filters.attendance import AttendenceFilter



class CreateListMixin:
    """Allows bulk creation of a resource."""
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

class StudentAttendenceView(CreateListMixin, ModelViewSet):
    serializer_class = StudentAttendenceModelSerializer
    queryset = StudentAttendenceModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = AttendenceFilter
    # permission_classes = 

    def sendSMS(self, numbers, message):
        data =  urllib.parse.urlencode({'apikey': "1VA4w/9tWbs-70MZ4dvgXfl7HMg5ONWRZcBlJY72T6", 'numbers': numbers,
            'message' : message, 'sender': "TXTLCL"})
        data = data.encode('utf-8')
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        f = urllib.request.urlopen(request, data)
        fr = f.read()
        return fr

    def create(self, request):

        data = request.data
        if isinstance(data,(list,)):
            for student in data:
                if student['attended'] == False:
                    msg = "Pls Note:\n Your ward " +  student['name'] + " is absent on " + str(datetime.now) +"\nPrincipal\n Futurastic"
                    numbers = [student['number']]
                    response = self.sendSMS(numbers, msg)
                    print(response)

        return super().create(request)

    @list_route(methods=['get'])
    def count(self, *args, **kwargs):
        count = StudentAttendenceModel.objects.filter(attended=True).annotate(week_num=ExtractWeek('date')).values('week_num').annotate(count=Count('week_num'))
        return Response(status=status.HTTP_200_OK, data={"count":count})