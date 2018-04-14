from django_filters import FilterSet, NumberFilter
from ..models.student import StudentModel


class StudentFilter(FilterSet):
    class Meta:
        model = StudentModel
        fields = ['school']
        