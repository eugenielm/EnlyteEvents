from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import UpdateAPIView, ListAPIView

from .filters import EventFilter
from .models import Event
from .serializers import EventSerializer



class EventUpdateView(UpdateAPIView):
    """
    API endpoint that allows an event to be edited.
    Use the `PATCH` method for partial update, or `PUT` for updating all required fields 
    (EventSerializer's fields, i.e. `name`, `organization`, `start_date`, `cost`).
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class EventsListView(ListAPIView):
    """
    Returns Event instances matching a search against all Event's fields (except `initial_id`)
    and/or filtering Event instances by:
    `name`, `organization`, `exact_cost`, `max_cost`, `exact_date`, `exact_date`, `before_date`.
    Returns all Event instances if no search/filter is applied.
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    # https://www.django-rest-framework.org/api-guide/filtering/#generic-filtering
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    filterset_class = EventFilter
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    search_fields = ('name', 'start_date', 'organization', 'cost')
    ordering_fields = '__all__'
    ordering = ('name', 'start_date', 'organization', 'cost')