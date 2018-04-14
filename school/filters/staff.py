from django_filters import FilterSet, NumberFilter
from ..models.staff import StaffModel


class StaffFilter(FilterSet):
    class Meta:
        model = StaffModel
        fields = ['school']
