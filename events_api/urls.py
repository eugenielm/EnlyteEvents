
from . import views
from django.urls import re_path
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer


# https://www.django-rest-framework.org/api-guide/schemas/#the-get_schema_view-shortcut
schema_view = get_schema_view(
    title="Events API",
    renderer_classes=[JSONOpenAPIRenderer,]
)

urlpatterns = [
    re_path(r'^events/(?P<pk>\d+)/?$', views.EventUpdateView.as_view()),
    re_path(r'^events/?$', views.EventsListView.as_view()),
    re_path(r'^schema/?$', schema_view),
]