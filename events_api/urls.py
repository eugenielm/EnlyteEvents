
from . import views
from django.urls import path


urlpatterns = [
    path('events/<int:pk>/', views.EventUpdateView.as_view()),
]