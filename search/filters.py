import django_filters
from django_filters import DateFilter, CharFilter
from .models import Advertisment

class AdvertismentFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    name_c = CharFilter(field_name='name', lookup_expr='icontains')
    descriptions_c = CharFilter(field_name='descriptions', lookup_expr='icontains')

    class Meta:
        model = Advertisment
        fields = ['name', 'description', 'capacity', 'conditions']
