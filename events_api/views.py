from rest_framework.generics import UpdateAPIView
from .serializers import EventSerializer
from .models import Event


class EventUpdateView(UpdateAPIView):
    """
    API endpoint that allows an event to be edited.
    Use the `PATCH` method for partial update, or `PUT` for updating all required fields 
    (i.e. `name`, `organization`, `start_date`, `cost` - see EventSerializer's fields).
    """
    serializer_class = EventSerializer
    queryset = Event.objects.all()