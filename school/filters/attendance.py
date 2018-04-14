from django_filters import FilterSet, NumberFilter
from ..models.attendence import StudentAttendenceModel


class AttendenceFilter(FilterSet):
    month = NumberFilter(name='date', lookup_expr='month__exact')
    # y = django_filters.NumberFilter(name='date', lookup_expr='year')
    class Meta:
        model = StudentAttendenceModel
        fields = ['student', 'attended', 'date', 'modified_date', 'student__class_session__session',
         'student__class_session__class_id','student__class_session__incharge', 'student__student', 'month']