from django_filters import FilterSet, NumberFilter
from ..models.subject import SubjectModel


class SubjectFilter(FilterSet):
    class Meta:
        model = SubjectModel
        fields = ['school', 'code', 'name']
        