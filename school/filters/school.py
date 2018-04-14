from django_filters import FilterSet, NumberFilter
from ..models.school import SchoolModel


class SchoolFilter(FilterSet):
    class Meta:
        model = SchoolModel
        fields = '__all__'