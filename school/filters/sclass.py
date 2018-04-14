from django_filters import FilterSet, NumberFilter
from ..models.sclass import ClassModel


class ClassFilter(FilterSet):
    class Meta:
        model = ClassModel
        fields = ['section', 'name', 'school']