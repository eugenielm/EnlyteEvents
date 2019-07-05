import django_filters
from .models import Event


# https://django-filter.readthedocs.io/en/latest/guide/usage.html#the-filter
class EventFilter(django_filters.FilterSet):
    # https://django-filter.readthedocs.io/en/latest/guide/usage.html#declaring-filters
    # use of declarative filters instead of generating filters with Meta.fields for more flexibility
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    organization = django_filters.CharFilter(field_name='organization', lookup_expr='icontains')
    exact_cost = django_filters.NumberFilter(field_name='cost')
    max_cost = django_filters.NumberFilter(field_name='cost', lookup_expr='lte')
    exact_date = django_filters.DateTimeFilter(field_name='start_date')
    from_date = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='gte')
    before_date = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='lt')

    class Meta:
        model = Event
        fields = ['name', 'organization', 'exact_cost', 'max_cost', 'exact_date', 'from_date', 'before_date']
        # also possible but less flexible with query parameter names:
        # https://django-filter.readthedocs.io/en/latest/guide/usage.html#generating-filters-with-meta-fields
        # fields = {
        #     'name': ['icontains'],
        #     'organization': ['icontains'],
        #     'cost': ['exact', 'lt'],
        #     'start_date': ['exact',],
        # }
